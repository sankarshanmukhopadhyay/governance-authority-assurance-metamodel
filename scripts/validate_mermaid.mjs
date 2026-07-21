#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const excluded = new Set([".git", "node_modules", "_site", "vendor", "packages"]);
const results = [];

async function markdownFiles(directory) {
  const files = [];
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    if (excluded.has(entry.name)) continue;
    const full = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await markdownFiles(full));
    else if (entry.isFile() && entry.name.endsWith(".md")) files.push(full);
  }
  return files;
}

function blocksFrom(markdown) {
  const blocks = [];
  const pattern = /^```mermaid\s*\n([\s\S]*?)^```\s*$/gm;
  let match;
  while ((match = pattern.exec(markdown)) !== null) {
    const line = markdown.slice(0, match.index).split("\n").length;
    blocks.push({ source: match[1].trim(), line });
  }
  return blocks;
}

// Mermaid sanitises labels while parsing. Provide a browser-compatible DOM
// so the same parser path used by the published site can run in Node CI.
const { JSDOM } = await import("jsdom");
const dom = new JSDOM("<!doctype html><html><body></body></html>");
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const { default: mermaid } = await import("mermaid");
mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
const files = await markdownFiles(root);
let diagrams = 0;
let failures = 0;

for (const file of files.sort()) {
  const markdown = await fs.readFile(file, "utf8");
  const blocks = blocksFrom(markdown);
  for (let index = 0; index < blocks.length; index += 1) {
    diagrams += 1;
    const block = blocks[index];
    try {
      await mermaid.parse(block.source);
      results.push({ file: path.relative(root, file), block: index + 1, line: block.line, status: "pass" });
    } catch (error) {
      failures += 1;
      results.push({
        file: path.relative(root, file),
        block: index + 1,
        line: block.line,
        status: "fail",
        error: error?.message ?? String(error)
      });
    }
  }
}

const evidence = {
  mermaidVersion: "11.16.0",
  status: failures === 0 ? "pass" : "fail",
  markdownFilesChecked: files.length,
  diagramsChecked: diagrams,
  passed: diagrams - failures,
  failed: failures,
  results
};
await fs.mkdir(path.join(root, "validation"), { recursive: true });
await fs.writeFile(path.join(root, "validation", "mermaid-validation.json"), `${JSON.stringify(evidence, null, 2)}\n`);

if (failures) {
  console.error(`Mermaid validation: FAIL (${failures} of ${diagrams} diagrams)`);
  for (const result of results.filter((item) => item.status === "fail")) {
    console.error(`- ${result.file}:${result.line} block ${result.block}: ${result.error}`);
  }
  process.exit(1);
}
console.log(`Mermaid validation: PASS (${diagrams} diagrams across ${files.length} Markdown files; Mermaid 11.16.0)`);

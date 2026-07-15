# Implementation Guide

This guide is informative. The normative specification controls conformance.

## Step 1: Establish governance context

Identify the institutional, contractual, legal and operational environment. Define which effects are consequential, which actors participate, which affected parties exist and which authorities may establish policy.

## Step 2: Model roles and authority

For each role, document eligibility, authority source, scope, constraints, obligations, activation, suspension and termination. Do not use authentication or registry inclusion as a substitute for authority semantics.

## Step 3: Model delegation paths

Represent delegator, delegate, originating principal, parent delegation, scope, purpose, validity, redelegation rights and revocation propagation. Test that no child delegation exceeds its valid parent authority.

## Step 4: Define evidence and assurance

For each consequential decision class, state which claims may be relied upon, acceptable evidence, provenance, freshness, verification method and assurance threshold.

## Step 5: Create runtime decision points

Before an effect is admitted, evaluate actor identity, authority, delegation lineage, policy, evidence, status, risk, boundary crossings and required human review. Re-evaluate during execution when material conditions can change.

## Step 6: Produce decision receipts

Record the proposed effect, decision outcome, evaluated authority, policy version, evidence references, assurance state, decision-maker, time and accountable parties. Apply minimisation and access controls.

## Step 7: Govern lifecycle and failure

Define issuance, activation, suspension, revocation, expiry, remediation and archival events. Ensure stale or unverifiable state leads to an explicit denial, restriction, suspension or escalation outcome.

## Step 8: Add redress

Provide correction, review, appeal and remedy paths. Specify who can halt, reverse or remediate effects, what evidence is available and how affected parties are notified.

## Step 9: Select profiles

Apply the Foundation Profile to every implementation and add specialised profiles for delegation, agents, runtime governance, trust graphs and continuous assurance.

## Step 10: Publish a conformance statement

List the specification version, profiles, conformance targets, exclusions, implementation identifiers, test evidence and unresolved limitations.

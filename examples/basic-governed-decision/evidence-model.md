---
title: "Evidence and Assurance Model"
nav_exclude: true
artifact_type: Informative implementation pattern
normative_status: Informative
---
# Evidence and Assurance Model

## Purpose

This page explains the evidence and assurance model for the **Basic Governed Decision** pattern.

## Required controls

- The governing source and accountable party are explicit.
- Authority and evidence are current, scoped and attributable.
- Lifecycle transitions have authorised initiators and observable effects.
- Enforcement fails safely when required state cannot be established.
- Review and remedy remain reachable for affected parties.

## Operational interpretation

Implementations should represent each transition as a governance event, retain evidence sufficient to reconstruct the decision, and distinguish institutional authority from technical control. Dependencies must be explicit so suspension, revocation, correction and remedy can propagate without relying on undocumented operator knowledge.

## Evidence expectations

Evidence should identify the relevant requirement, source, actor, time, state, decision and accountable authority. Sensitive evidence should be minimised or access-controlled without making meaningful challenge impossible.

## Failure conditions

A missing authority source, stale state, unsupported delegation, unresolved conflict, absent accountable party or unavailable remedy route must not be silently treated as permission.

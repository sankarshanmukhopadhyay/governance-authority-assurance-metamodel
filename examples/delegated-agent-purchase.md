# Example: Delegated Agent Purchase

A person authorises a purchasing agent to order office supplies up to a monthly value limit. The agent may use an approved marketplace tool but may not create sub-agents or purchase restricted categories.

## Governance mapping

- **Principal:** the purchaser.
- **Delegate:** the purchasing agent.
- **Authority:** purchase approved categories for the stated purpose.
- **Constraints:** monthly limit, approved merchants, no redelegation, defined validity period.
- **Evidence:** delegation record, merchant status, budget state and product classification.
- **Decision:** permit, deny or route for approval.
- **Receipt:** records authority, policy, evidence references, amount and outcome.
- **Accountability:** purchaser and operating service remain attributable; disputed purchases enter the review process.

The example demonstrates why account access is not authority. The agent may technically access a payment method while lacking authority for a particular category or amount.

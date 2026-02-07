# ticketmind/agent/policies/policy_docs.py

POLICIES = [

    {
        "id": "faq_policy_v1",
        "title": "FAQ and Informational Request Policy",
        "content": """
Requests classified as FAQ or informational may be handled automatically
if the user is classified as LOW or MEDIUM risk.

Automatic responses are allowed for general product information,
usage instructions, and publicly available documentation.

Automatic responses must not include internal system details,
security mechanisms, or confidential operational information.

If the request involves ambiguity, legal interpretation,
or personal data modification, escalation to a human agent is required.
"""
    },

    {
        "id": "refund_policy_v1",
        "title": "Refund Policy",
        "content": """
Customers may request a refund within 24 hours of purchase
if the product or service has not been fully consumed.

Refunds may be issued automatically only for users classified as LOW risk.

Users classified as MEDIUM or HIGH fraud risk must not receive
automatic refunds and require human review.

VIP status may allow exceptions to refund timing,
but does not override fraud prevention rules.

All refund actions must be logged for audit purposes.
"""
    },

    {
        "id": "fraud_policy_v1",
        "title": "Fraud and Risk Assessment Policy",
        "content": """
Fraud risk is determined based on historical user behavior,
including refund frequency, chargeback history,
account age, and purchase patterns.

Users classified as HIGH risk must not receive
automatic financial actions or account-level changes.

Any action involving financial impact for HIGH risk users
must be escalated to a human agent.

Fraud prevention rules take priority over customer convenience.
"""
    },

    {
        "id": "privacy_policy_v1",
        "title": "Privacy and Data Usage Policy",
        "content": """
Users may request information about how their personal data
is collected, stored, and processed.

Automatic responses are allowed for general explanations
based on publicly available privacy policies.

The system must not disclose internal security mechanisms,
data processing internals, or proprietary algorithms.

Requests related to data deletion, data export,
or legal rights must be escalated to a human agent.
"""
    },

    {
        "id": "escalation_policy_v1",
        "title": "Escalation Policy",
        "content": """
Requests must be escalated to a human agent if
the automated system confidence is below the acceptable threshold.

Actions involving refunds, bans, chargebacks,
or legal matters require escalation when risk is MEDIUM or HIGH.

Conflicting policy guidance must always be resolved
through human review.

Escalation decisions must prioritize fraud prevention,
user safety, and regulatory compliance.
"""
    },

    {
        "id": "vip_policy_v1",
        "title": "VIP User Handling Policy",
        "content": """
VIP users are entitled to prioritized handling
and faster response times.

VIP status does not override fraud prevention rules,
chargeback restrictions, or legal obligations.

Exceptional requests from VIP users involving
financial or account-level actions require manual review.

All VIP-related exceptions must be logged and auditable.
"""
    },

]

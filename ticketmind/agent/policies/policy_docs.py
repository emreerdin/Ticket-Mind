"""
Policy definitions for TicketMind.

Policies are:
- deterministic
- intent-scoped
- cumulative (all retrieved policies apply)
"""

POLICIES = [
    {
        "id": "faq_policy_v1",
        "intent": "FAQ",
        "title": "FAQ Handling Policy",
        "content": """
FAQ requests may be handled automatically if the user risk level is LOW or MEDIUM.
Responses must be informational only.
No sensitive personal or financial data may be disclosed.
High risk users must be escalated to human review.
""",
        "allowed_actions": ["AUTO_REPLY", "ESCALATE"],
    },

    {
        "id": "privacy_policy_v1",
        "intent": "FAQ",
        "title": "Privacy & Data Usage Policy",
        "content": """
Privacy related questions may be answered automatically.
Responses must not expose internal data handling mechanisms.
Personal data details must not be disclosed.
If the request asks for account-specific data, escalation is required.
""",
        "allowed_actions": ["AUTO_REPLY", "ESCALATE"],
    },

    {
        "id": "refund_policy_v1",
        "intent": "REFUND",
        "title": "Refund Policy",
        "content": """
Refunds may be issued automatically only if:
- Risk level is LOW
- No previous chargebacks
- Refund count is below threshold

Medium or High risk users must be escalated.
""",
        "allowed_actions": ["REFUND", "ESCALATE"],
    },

    {
        "id": "fraud_policy_v1",
        "intent": "REFUND",
        "title": "Fraud Prevention Policy",
        "content": """
If fraud risk is HIGH, refunds must not be processed automatically.
All high-risk refund requests require human approval.
""",
        "allowed_actions": ["ESCALATE"],
    },

    {
        "id": "account_policy_v1",
        "intent": "ACCOUNT",
        "title": "Account Management Policy",
        "content": """
Account related requests may be handled automatically if no security risk is detected.
Sensitive operations require escalation.
""",
        "allowed_actions": ["AUTO_REPLY", "ESCALATE"],
    },

    {
        "id": "chargeback_policy_v1",
        "intent": "CHARGEBACK",
        "title": "Chargeback Handling Policy",
        "content": """
Chargeback related issues must always be escalated.
No automatic actions are permitted.
""",
        "allowed_actions": ["ESCALATE"],
    },

    {
        "id": "technical_policy_v1",
        "intent": "TECHNICAL",
        "title": "Technical Support Policy",
        "content": """
Technical issues may be answered automatically with troubleshooting steps.
If the issue persists or involves billing or account security, escalation is required.
""",
        "allowed_actions": ["AUTO_REPLY", "ESCALATE"],
    },

    {
        "id": "global_safety_policy_v1",
        "intent": "ANY",
        "title": "Global Safety Policy",
        "content": """
If the system is uncertain or policies conflict, escalate to human review.
""",
        "allowed_actions": ["ESCALATE"],
    },
]


def get_policies_for_intent(intent: str):
    """
    Retrieve all policies relevant to a given intent.
    Includes intent-specific and global policies.
    """
    return [
        p for p in POLICIES
        if p["intent"] == intent or p["intent"] == "ANY"
    ]

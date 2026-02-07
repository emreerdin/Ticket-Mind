def handle_decide_action(context: dict):
    intent = context["intent"]
    risk = context["risk"]
    policies = context["policies"]

    # ❌ wrong: context["body"]
    # ✅ correct:
    body = context["ticket"]["body"]

    allowed_actions = set()

    for policy in policies:
        text = policy["content"].lower()

        if intent == "FAQ":
            if risk["label"] in {"LOW", "MEDIUM"}:
                allowed_actions.add("AUTO_REPLY")

        if "must be escalated" in text:
            allowed_actions.add("ESCALATE")

    if not allowed_actions:
        allowed_actions.add("ESCALATE")

    action = (
        "AUTO_REPLY" if "AUTO_REPLY" in allowed_actions
        else "ESCALATE"
    )

    context["decision"] = {
        "action": action,
        "allowed_actions": list(allowed_actions),
        "policy_ids": [p["id"] for p in policies],
    }

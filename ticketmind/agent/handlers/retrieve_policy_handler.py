from ticketmind.agent.policies.policy_docs import get_policies_for_intent

def handle_retrieve_policy(context: dict):
    intent = context["intent"]

    # ❌ wrong: context["body"]
    # ✅ correct:
    body = context["ticket"]["body"]

    policies = get_policies_for_intent(intent)

    context["policies"] = policies

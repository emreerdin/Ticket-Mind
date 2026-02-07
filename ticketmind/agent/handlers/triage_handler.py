from ticketmind.llm.classifiers import triage_classifier

def handle_triage(context: dict) -> str:
    ticket = context["ticket"]

    intent = triage_classifier.triage_classify(
        ticket_body=ticket["body"],
        is_offline=False
    )

    if not intent:
        raise RuntimeError("Triage failed")

    return intent

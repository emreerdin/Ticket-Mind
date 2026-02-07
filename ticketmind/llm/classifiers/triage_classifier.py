from ticketmind.llm.llm_caller import llm_call
from ticketmind.llm.prompts.triage_prompt import build_classification_prompt
import json

def triage_classify(ticket_body: str, *, is_offline=False) -> str:
    raw = llm_call(build_classification_prompt(ticket_body), is_offline=is_offline)

    label = raw.strip().upper()

    if label not in {
        "REFUND", "BAN", "TECHNICAL", "FAQ",
        "CHARGEBACK", "ACCOUNT", "OTHER"
    }:
        raise RuntimeError(f"Invalid triage label: {raw}")

    return label

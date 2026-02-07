from ticketmind.llm.llm_caller import llm_call
from ticketmind.llm.prompts.spam_prompt import build_spam_prompt
import json

def spam_classify(ticket_body: str, *, is_offline=False) -> str:
    raw = llm_call(build_spam_prompt(ticket_body), is_offline=is_offline)

    label = raw.strip().upper()

    if label not in {"SPAM", "HAM"}:
        raise RuntimeError(f"Invalid spam label: {raw}")

    return label


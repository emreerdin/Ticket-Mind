SPAM_CLASSIFICATION_SYSTEM_PROMPT = """
Classify the following ticket as either:

SPAM
HAM

Rules:
- SPAM includes advertising, promotions, SEO offers, crypto scams, meaningless or bot-like messages.
- HAM includes legitimate customer support requests, even if unclear or poorly written.

Return ONLY one of the two labels.
Do not return anything else.
"""

def build_spam_prompt(ticket_body: str) -> str:
    return SPAM_CLASSIFICATION_SYSTEM_PROMPT + "\n\n" + ticket_body

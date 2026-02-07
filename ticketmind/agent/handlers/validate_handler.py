from ticketmind.llm.classifiers.spam_classifier import spam_classify

def handle_validation(context: dict):
    ticket = context["ticket"]
    body = ticket["body"]   # ✅ correct

    result = spam_classify(body)
    if result != "HAM":
        raise RuntimeError("Spam ticket")

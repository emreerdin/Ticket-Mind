CLASSIFICATION_SYSTEM_PROMPT = """
Please choose the closest ticket type for the following sentence as follows: 
REFUND/BAN/TECHNICAL/FAQ/CHARGEBACK/ACCOUNT/OTHER

And only return the type. Nothing else.
"""

def build_classification_prompt(type:str):
    return f"{CLASSIFICATION_SYSTEM_PROMPT}" + type
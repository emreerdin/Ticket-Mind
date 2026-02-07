from enum import Enum, auto

class TicketState(Enum):  # ✅ PascalCase (Python convention)
    WAITING = auto()
    INGEST = auto()          # System receives raw ticket
    VALIDATE = auto()        # Input validation (spam, duplicate, completeness)
    ENRICH = auto()          # Gather user context (profile, fraud risk)
    RETRIEVE_POLICY = auto() # Search relevant policies (RAG)
    TRIAGE = auto()          # Classify ticket (REFUND, BAN, TECHNICAL, FAQ)
    DECIDE_ACTION = auto()   # Determine action + confidence
    DRAFT_RESPONSE = auto()  # Generate response text
    SAFETY_CHECK = auto()    # Risk assessment (dangerous action?)
    HUMAN_APPROVAL = auto()  # Wait for human decision
    EXECUTE_TOOLS = auto()   # Run approved tools (refund, email, etc.)
    CLOSE = auto()           # Successfully completed
    FAILED = auto()          # Unrecoverable error
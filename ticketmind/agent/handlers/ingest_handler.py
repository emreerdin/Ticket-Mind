from ticketmind.db.repos import tickets_repo, agent_runs
from ticketmind.llm import llm_caller
import uuid

def handle_ingest(fsm_state):
    tickets = tickets_repo.get_open_tickets()
    if not tickets:
        raise RuntimeError("No open tickets found")

    raw_ticket = tickets[0]

    # 🔹 Normalize ticket schema (CRITICAL)
    ticket = {
        "id": raw_ticket["id"],
        "user_id": raw_ticket["user_id"],
        "subject": raw_ticket.get("subject"),
        "body": raw_ticket.get("body") or raw_ticket.get("description"),
        "status": raw_ticket.get("status"),
        "created_at": raw_ticket.get("created_at"),
    }

    if not ticket["body"]:
        raise RuntimeError("Ticket body is missing")

    trace_id = uuid.uuid4()
    agent_name = llm_caller.model_name

    agent_runs.insert_agent_run(
        agent_name=agent_name,
        trace_id=trace_id,
        ticket_id=ticket["id"],
        state=fsm_state,
    )

    return {
        "ticket": ticket,
        "trace_id": trace_id,
    }

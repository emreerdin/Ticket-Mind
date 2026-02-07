from ticketmind.agent.agent_fsm import FSM
from ticketmind.agent.states import TicketState
from ticketmind.db.repos import tickets_repo

fsm = FSM()

while fsm.current_state not in {TicketState.CLOSE, TicketState.FAILED}:
    fsm.step()

print("FINAL STATE:", fsm.current_state)

if fsm.current_state == TicketState.FAILED:
    print("ERROR:", fsm.context.get("error"))
else:
    print("DECISION:", fsm.context["decision"])


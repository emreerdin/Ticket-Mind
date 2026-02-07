from ticketmind.agent.states import TicketState
from ticketmind.agent.handlers import (
    ingest_handler,
    validate_handler,
    triage_handler,
    enrich_handler,
    retrieve_policy_handler,
    decide_handler,
)

TRANSITIONS = {
    TicketState.WAITING:         [TicketState.INGEST, TicketState.FAILED],
    TicketState.INGEST:          [TicketState.VALIDATE, TicketState.FAILED],
    TicketState.VALIDATE:        [TicketState.TRIAGE, TicketState.FAILED],
    TicketState.TRIAGE:          [TicketState.ENRICH, TicketState.FAILED],
    TicketState.ENRICH:          [TicketState.RETRIEVE_POLICY, TicketState.FAILED],
    TicketState.RETRIEVE_POLICY: [TicketState.DECIDE_ACTION, TicketState.FAILED],
    TicketState.DECIDE_ACTION:   [TicketState.CLOSE, TicketState.FAILED],
}

class FSM:
    def __init__(self):
        self.current_state = TicketState.WAITING
        self.context = {}

    def _transition(self, next_state: TicketState):
        if next_state not in TRANSITIONS[self.current_state]:
            raise RuntimeError(
                f"Invalid transition: {self.current_state} → {next_state}"
            )
        self.current_state = next_state

    def step(self):
        state = self.current_state

        try:
            if state == TicketState.WAITING:
                self.context = ingest_handler.handle_ingest(state)
                self._transition(TicketState.INGEST)

            elif state == TicketState.INGEST:
                print("DEBUG CONTEXT AFTER INGEST:", self.context)
                validate_handler.handle_validation(self.context)
                self._transition(TicketState.VALIDATE)

            elif state == TicketState.VALIDATE:
                intent = triage_handler.handle_triage(self.context)
                self.context["intent"] = intent
                self._transition(TicketState.TRIAGE)

            elif state == TicketState.TRIAGE:
                enrich_handler.handle_enrich(self.context)
                self._transition(TicketState.ENRICH)

            elif state == TicketState.ENRICH:
                retrieve_policy_handler.handle_retrieve_policy(self.context)
                self._transition(TicketState.RETRIEVE_POLICY)

            elif state == TicketState.RETRIEVE_POLICY:
                self._transition(TicketState.DECIDE_ACTION)

            elif state == TicketState.DECIDE_ACTION:
                decide_handler.handle_decide_action(self.context)
                self._transition(TicketState.CLOSE)



            return self.current_state

        except Exception as e:
            # ensure context always exists
            if self.context is None:
                self.context = {}
            self.context["error"] = str(e)
            self.current_state = TicketState.FAILED
            return self.current_state

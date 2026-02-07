# TicketMind — Policy-Aware Deterministic AI Agent

TicketMind is a **policy-aware, deterministic AI agent** for processing customer support tickets using a **finite state machine (FSM)**, **explicit policies**, and **controlled LLM usage**.

Unlike prompt-only or chain-based "agents", TicketMind explicitly separates:
- Perception (classification)
- Context enrichment (user profile and risk)
- Normative constraints (policies)
- Decision-making (allowed actions)
- Control flow (FSM)

This design makes the system **auditable, explainable, and production-oriented**.

---

## Key Features

- Deterministic finite state machine controlling execution
- Input validation and spam detection
- Intent classification (FAQ, REFUND, TECHNICAL, etc.)
- User enrichment and risk scoring
- Explicit policy enforcement
- Fail-closed behavior (illegal transitions are blocked)
- Explainable decisions (policy IDs attached to actions)

---

## Architecture Overview

```
WAITING
  ↓
INGEST
  ↓
VALIDATE
  ↓
TRIAGE
  ↓
ENRICH
  ↓
RETRIEVE_POLICY
  ↓
DECIDE_ACTION
  ↓
CLOSE
```

Each state:
- Performs exactly one responsibility
- Mutates a shared `context` object
- Transitions only if explicitly allowed by FSM rules

---

## What Makes This an Agent

TicketMind qualifies as an agent because it:

1. **Perceives the environment**  
   (ticket text, user data, historical signals)

2. **Reasons under constraints**  
   (explicit policies limit what actions are allowed)

3. **Decides actions autonomously**  
   (`AUTO_REPLY`, `ESCALATE`, `REFUND`, etc.)

4. **Acts over time**  
   (multi-step FSM, not a single function call)

5. **Fails safely**  
   (invalid transitions and missing data halt execution)

Policies are never selected arbitrarily.  
All relevant policies apply **cumulatively** to constrain decisions.

---

## Project Structure

```
ticketmind/
├── agent/
│   ├── contracts/
│   │   └── ticket_input.py
│   ├── domain/
│   │   └── risk.py
│   ├── handlers/
│   │   ├── decide_handler.py
│   │   ├── enrich_handler.py
│   │   ├── ingest_handler.py
│   │   ├── retrieve_policy_handler.py
│   │   ├── triage_handler.py
│   │   └── validate_handler.py
│   ├── policies/
│   ├── agent_fsm.py
│   └── states.py
│
├── db/
│   ├── migrations/
│   ├── repos/
│   │   ├── agent_runs.py
│   │   ├── tickets_repo.py
│   │   └── users_repo.py
│   └── connection.py
│
├── llm/
│   ├── classifiers/
│   │   ├── spam_classifier.py
│   │   └── triage_classifier.py
│   ├── prompts/
│   │   ├── decision_prompt.py
│   │   ├── spam_prompt.py
│   │   └── triage_prompt.py
│   └── llm_caller.py
│
├── pytest/
│   └── main.py
│
├── ui/
│   └── app.py
│
└── ticketmind_venv/
```

---

## How to Run

```bash
python pytest/main.py
```

The FSM runs until it reaches either `CLOSE` or `FAILED`.

---

## Expected Demo Outputs

### Demo 1 — FAQ / Privacy Question (Low Risk)

**Input ticket:**

```json
{
  "subject": "Privacy concern",
  "body": "How is my data being used?"
}
```

**FSM result:**

```
FINAL STATE: TicketState.CLOSE
```

**Decision:**

```json
{
  "action": "AUTO_REPLY",
  "allowed_actions": ["AUTO_REPLY", "ESCALATE"],
  "policy_ids": [
    "faq_policy_v1",
    "privacy_policy_v1",
    "global_safety_policy_v1"
  ]
}
```

This ticket is handled automatically because:
- Risk is low
- FAQ and privacy policies allow auto-replies
- No policy forbids the action

---

### Demo 2 — High-Risk Refund Request

**Input ticket:**

```json
{
  "subject": "Refund request",
  "body": "I want my money back immediately"
}
```

**User context:**

```json
{
  "refund_count": 5,
  "chargeback_count": 2,
  "risk_label": "HIGH"
}
```

**Decision:**

```json
{
  "action": "ESCALATE",
  "allowed_actions": ["ESCALATE"],
  "policy_ids": [
    "refund_policy_v1",
    "fraud_policy_v1",
    "global_safety_policy_v1"
  ]
}
```

Automatic refunds are blocked due to elevated fraud risk.  
The ticket is escalated for human review.

---

### Demo 3 — Spam Ticket

**Input:**

```json
{
  "body": "Best SEO services cheap crypto promo!!!"
}
```

**FSM result:**

```
FINAL STATE: TicketState.FAILED
ERROR: Spam ticket
```

Spam is detected during validation and the system terminates safely.

---

## Design Principles

- **Determinism over hallucination**
- **Policies over prompts**
- **FSM over ad-hoc chaining**
- **LLMs assist but never override rules**

---

## Possible Extensions (V2)

- Draft response generation
- Hybrid policy retrieval (intent-gated + vector search)
- Human-in-the-loop approval
- Tool execution (refunds, email, ticket creation)
- Trace replay and observability

---

## Why This Matters

TicketMind demonstrates how to build agentic systems that:

- Are controllable and auditable
- Scale beyond demos
- Respect business and safety constraints
- Avoid uncontrolled LLM decision-making

This repository is intentionally minimal, explicit, and principled.

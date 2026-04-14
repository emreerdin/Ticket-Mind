# Ticket-Mind

> Policy-aware, deterministic AI agent for customer support ticket processing — FSM controls execution, LLM assists classification.

---

## Problem

Most AI support systems hand ticket routing directly to the LLM. That means decisions vary with phrasing, policies get ignored under edge cases, and there's no audit trail.

Ticket-Mind separates concerns explicitly: the LLM classifies, the FSM decides, and policies constrain every action. The result is a system that's explainable, auditable, and production-safe.

---

## Architecture

```
Ticket Input
    ↓
INGEST       — receive and parse ticket
    ↓
VALIDATE     — input validation + spam detection
    ↓
TRIAGE       — LLM intent classification (FAQ / REFUND / TECHNICAL / ...)
    ↓
ENRICH       — user profile fetch + risk scoring
    ↓
RETRIEVE_POLICY — load all applicable policies cumulatively
    ↓
DECIDE_ACTION   — determine allowed action under policy constraints
    ↓
CLOSE        — execute action + log decision with policy IDs
```

Each state has exactly one responsibility. Transitions only occur if explicitly permitted by FSM rules. Invalid transitions halt execution — the system fails safe.

---

## Why This Is an Agent

Ticket-Mind qualifies as an agent because it:

- **Perceives** its environment (ticket text, user data, historical signals)
- **Reasons under constraints** (explicit policies limit which actions are allowed)
- **Decides autonomously** (`AUTO_REPLY`, `ESCALATE`, `REFUND`, etc.)
- **Operates over time** (multi-step FSM, not a single function call)
- **Fails safely** (invalid transitions and missing data halt execution)

---

## Design Principles

| Principle | Implementation |
|---|---|
| Determinism over hallucination | FSM controls all state transitions |
| Policies over prompts | Every decision is constrained by explicit policy rules |
| FSM over ad-hoc chaining | No uncontrolled LLM-to-LLM calls |
| LLM assists, never overrides | LLM output is input to FSM, not a final decision |

---

## Module Overview

| Module | Responsibility |
|---|---|
| `agent/agent_fsm.py` | FSM core — state transitions and execution loop |
| `agent/handlers/` | One handler per FSM state |
| `agent/policies/` | Policy definitions — constrain allowed actions |
| `agent/domain/risk.py` | Risk scoring logic |
| `llm/classifiers/` | Spam detection + intent classification |
| `llm/prompts/` | Structured prompts for each LLM task |
| `db/repos/` | Ticket, user, and agent run persistence |
| `ui/app.py` | Streamlit interface |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Gemini](https://img.shields.io/badge/Gemini-2.0_flash-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)

---

## Status

This repository is a system overview. Source code is available upon request.  
For inquiries → [emreerdin.com/contact](https://www.emreerdin.com/contact)

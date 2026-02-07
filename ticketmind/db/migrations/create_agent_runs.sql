CREATE TABLE agent_runs (
    run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    trace_id UUID NOT NULL,

    ticket_id UUID NOT NULL REFERENCES tickets(id) ON DELETE CASCADE,

    current_state TEXT NOT NULL,

    context_jsonb JSONB NOT NULL DEFAULT '{}'::jsonb,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

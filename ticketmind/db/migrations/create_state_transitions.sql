CREATE TABLE state_transitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    run_id UUID NOT NULL
        REFERENCES agent_runs(run_id) ON DELETE CASCADE,

    from_state TEXT NOT NULL,
    to_state TEXT NOT NULL,

    timestamp TIMESTAMPTZ NOT NULL DEFAULT now(),

    data_jsonb JSONB NOT NULL DEFAULT '{}'::jsonb,

    duration_ms INTEGER
);

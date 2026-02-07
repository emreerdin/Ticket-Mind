CREATE TABLE tool_executions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    run_id UUID NOT NULL
        REFERENCES agent_runs(run_id) ON DELETE CASCADE,

    tool_name TEXT NOT NULL,

    input_jsonb JSONB NOT NULL DEFAULT '{}'::jsonb,
    output_jsonb JSONB NOT NULL DEFAULT '{}'::jsonb,

    success BOOLEAN NOT NULL,

    error_message TEXT,

    timestamp TIMESTAMPTZ NOT NULL DEFAULT now()
);

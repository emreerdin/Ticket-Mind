CREATE TABLE tickets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,

    -- Ticket content
    subject TEXT,
    body TEXT NOT NULL,

    -- Business-level lifecycle (NOT agent state)
    status TEXT NOT NULL DEFAULT 'OPEN'
        CHECK (status IN ('OPEN','CLOSED','DUPLICATE','CANCELLED')),

    -- Metadata (channel, device, etc.)
    metadata JSONB DEFAULT '{}'::jsonb,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO tickets (id, user_id, body, status, created_at)
SELECT
    t.id,
    u.user_id,
    t.body,
    'OPEN',
    t.created_at::timestamptz
FROM (
    VALUES
    -- Refund / Billing
    (gen_random_uuid(),'mega.whale@example.com','I was charged twice for my subscription renewal. Please refund the extra charge.','2026-01-26 19:10:01'),
    (gen_random_uuid(),'instant.refund@example.com','I was charged for a free trial. I want a refund.','2026-01-26 19:10:05'),
    (gen_random_uuid(),'refund.abuser@example.com','I want a refund for an item I already used.','2026-01-26 19:10:09'),
    (gen_random_uuid(),'problem.user@example.com','My refund was rejected but I believe it was valid.','2026-01-26 19:10:12'),
    (gen_random_uuid(),'serial.refunder@example.com','Wrong item received, refund me immediately.','2026-01-26 19:10:15'),

    -- Technical
    (gen_random_uuid(),'brand.new@example.com','Checkout page does not load on Android.','2026-01-26 19:11:01'),
    (gen_random_uuid(),'brand.new@example.com','Payment keeps failing even though my card works.','2026-01-26 19:11:04'),
    (gen_random_uuid(),'casual.gamer@example.com','Game stuck at loading screen 95%.','2026-01-26 19:11:07'),
    (gen_random_uuid(),'phone.gamer@example.com','App crashes when starting a ranked match.','2026-01-26 19:11:10'),
    (gen_random_uuid(),'mobile.only@example.com','In-game shop does not open on mobile data.','2026-01-26 19:11:13'),

    -- Ban / Fraud
    (gen_random_uuid(),'fraud.pattern@example.com','I was banned after winning a tournament.','2026-01-26 19:12:01'),
    (gen_random_uuid(),'problem.user@example.com','My account was banned because of a chargeback I did not do.','2026-01-26 19:12:05'),
    (gen_random_uuid(),'chargeback.user@example.com','Why was my account banned? I already paid everything.','2026-01-26 19:12:09'),
    (gen_random_uuid(),'refund.abuser@example.com','Unban my account immediately.','2026-01-26 19:12:12'),

    -- Gameplay
    (gen_random_uuid(),'active.player@example.com','Lost ranked points due to server disconnect.','2026-01-26 19:13:01'),
    (gen_random_uuid(),'steady.user@example.com','Matchmaking feels unfair lately.','2026-01-26 19:13:04'),
    (gen_random_uuid(),'reliable.user@example.com','Did not receive daily login rewards.','2026-01-26 19:13:07'),
    (gen_random_uuid(),'cross.platform@example.com','Progress is not synced between PC and mobile.','2026-01-26 19:13:10'),
    (gen_random_uuid(),'weekend.warrior@example.com','Event rewards were missing after completion.','2026-01-26 19:13:13'),

    -- Subscription
    (gen_random_uuid(),'premium.user@example.com','Canceled subscription but still charged.','2026-01-26 19:14:01'),
    (gen_random_uuid(),'inactive.user@example.com','I was charged even though I did not log in for months.','2026-01-26 19:14:04'),
    (gen_random_uuid(),'old.whale@example.com','VIP benefits are not applied to my account.','2026-01-26 19:14:07'),
    (gen_random_uuid(),'active.vip@example.com','VIP reward chest did not unlock.','2026-01-26 19:14:10'),

    -- Promo / Store
    (gen_random_uuid(),'normal.player@example.com','Promo code says already used but I never used it.','2026-01-26 19:15:01'),
    (gen_random_uuid(),'bundle.buyer@example.com','Bundle purchase did not deliver all items.','2026-01-26 19:15:04'),
    (gen_random_uuid(),'budget.gamer@example.com','Prices look higher on my account than my friend’s.','2026-01-26 19:15:07'),
    (gen_random_uuid(),'comeback.player@example.com','Returning player bonus not granted.','2026-01-26 19:15:10'),

    -- Mixed edge cases
    (gen_random_uuid(),'fraud.pattern@example.com','Gift sent by friend never arrived.','2026-01-26 19:16:01'),
    (gen_random_uuid(),'fraud.pattern@example.com','Suspicious activity detected on my account?','2026-01-26 19:16:04'),
    (gen_random_uuid(),'instant.refund@example.com','Refund processed but money not received.','2026-01-26 19:16:07'),
    (gen_random_uuid(),'problem.user@example.com','Support never replied to my previous ticket.','2026-01-26 19:16:10'),
    (gen_random_uuid(),'refund.abuser@example.com','Refund again, same issue as last time.','2026-01-26 19:16:13'),

    -- More noise for agent tests
    (gen_random_uuid(),'steady.user@example.com','Can you explain the ranking system?','2026-01-26 19:17:01'),
    (gen_random_uuid(),'reliable.user@example.com','How do I change my email address?','2026-01-26 19:17:04'),
    (gen_random_uuid(),'inactive.user@example.com','I forgot my password.','2026-01-26 19:17:07'),
    (gen_random_uuid(),'mobile.only@example.com','Notifications not working.','2026-01-26 19:17:10'),
    (gen_random_uuid(),'phone.gamer@example.com','Controller support not detected.','2026-01-26 19:17:13'),

    -- Final batch
    (gen_random_uuid(),'active.player@example.com','Latency spikes during peak hours.','2026-01-26 19:18:01'),
    (gen_random_uuid(),'active.vip@example.com','Priority support response is too slow.','2026-01-26 19:18:04'),
    (gen_random_uuid(),'old.whale@example.com','Account history missing before 2024.','2026-01-26 19:18:07'),
    (gen_random_uuid(),'budget.gamer@example.com','Any discounts coming soon?','2026-01-26 19:18:10'),
    (gen_random_uuid(),'just.joined@example.com','How do I start my first match?','2026-01-26 19:18:13')
) AS t(id, email, body, created_at)
JOIN users u ON u.email = t.email;

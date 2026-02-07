CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    total_spent NUMERIC(10,2) NOT NULL DEFAULT 0,
    purchase_count INT NOT NULL DEFAULT 0,
    last_purchase_date TIMESTAMPTZ,

    refund_count INT NOT NULL DEFAULT 0,
    total_refunded NUMERIC(10,2) NOT NULL DEFAULT 0,
    chargeback_count INT NOT NULL DEFAULT 0,

    vip_tier TEXT NOT NULL DEFAULT 'NONE',

    email TEXT NOT NULL,
    locale TEXT NOT NULL DEFAULT 'en_US',

    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


INSERT INTO users (
    total_spent, purchase_count, last_purchase_date,
    refund_count, total_refunded, chargeback_count,
    vip_tier, email, locale
) VALUES
(52000,120,'2026-01-26',0,0,0,'VIP','mega.whale@example.com','en_US'),
(1200,6,'2025-12-19',5,950,3,'BRONZE','problem.user@example.com','tr_TR'),
(2400,12,'2026-01-13',0,0,0,'BRONZE','normal.player@example.com','tr_TR'),
(18400,48,'2026-01-23',1,199,0,'GOLD','loyal.customer@example.com','tr_TR'),
(600,4,'2025-11-29',4,600,1,'BRONZE','serial.refunder@example.com','tr_TR'),
(0,0,NULL,0,0,0,'BRONZE','brand.new@example.com','tr_TR'),
(11200,34,'2026-01-21',0,0,0,'SILVER','active.vip@example.com','en_US'),
(1800,9,'2026-01-06',1,99,0,'BRONZE','casual.gamer@example.com','tr_TR'),
(299,1,'2026-01-23',1,299,0,'BRONZE','instant.refund@example.com','en_US'),
(8900,28,'2026-01-25',2,299,0,'SILVER','premium.user@example.com','de_DE'),
(850,5,'2025-10-30',3,550,2,'BRONZE','chargeback.user@example.com','tr_TR'),
(3200,14,'2026-01-18',1,149,0,'SILVER','regular.buyer@example.com','en_US'),
(15000,45,'2025-08-01',1,149,0,'GOLD','old.whale@example.com','tr_TR'),
(1100,8,'2025-12-29',7,900,1,'BRONZE','refund.abuser@example.com','en_US'),
(950,6,'2025-12-24',0,0,0,'BRONZE','weekend.player@example.com','en_GB'),
(9500,22,'2026-01-24',0,0,0,'SILVER','high.roller@example.com','en_GB'),
(1500,2,'2026-01-18',2,1500,1,'BRONZE','fraud.pattern@example.com','tr_TR'),
(4100,18,'2026-01-20',2,299,0,'SILVER','active.player@example.com','tr_TR'),
(2750,11,'2026-01-16',1,129,0,'SILVER','steady.user@example.com','en_US'),
(1300,8,'2026-01-03',0,0,0,'BRONZE','mobile.only@example.com','tr_TR'),
(2200,10,'2025-07-12',0,0,0,'BRONZE','inactive.user@example.com','tr_TR'),
(3500,15,'2026-01-23',1,199,0,'SILVER','comeback.player@example.com','de_DE'),
(1900,11,'2026-01-10',0,0,0,'BRONZE','reliable.user@example.com','tr_TR'),
(1500,8,'2026-01-22',1,99,0,'BRONZE','weekend.warrior@example.com','en_US'),
(0,0,NULL,0,0,0,'BRONZE','just.joined@example.com','tr_TR'),
(2800,7,'2026-01-14',0,0,0,'BRONZE','bundle.buyer@example.com','tr_TR'),
(3300,16,'2026-01-19',3,450,0,'SILVER','occasional.refunder@example.com','en_US'),
(1200,9,'2026-01-08',0,0,0,'BRONZE','phone.gamer@example.com','tr_TR'),
(4500,19,'2026-01-21',1,149,0,'SILVER','cross.platform@example.com','en_GB'),
(890,12,'2025-12-29',0,0,0,'BRONZE','budget.gamer@example.com','de_DE');

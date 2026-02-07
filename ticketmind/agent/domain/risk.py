from datetime import datetime, timezone

def calculate_risk(user: dict):
    score = 0.0
    reasons = []

    # 1️⃣ Chargeback = en ağır sinyal
    if user["chargeback_count"] >= 1:
        score += 0.5
        reasons.append("Has chargeback history")

    # 2️⃣ Refund yoğunluğu
    if user["refund_count"] >= 3:
        score += 0.3
        reasons.append("High refund count")

    # 3️⃣ Refund ratio (çok güçlü sinyal)
    if user["purchase_count"] > 0:
        refund_ratio = user["refund_count"] / user["purchase_count"]
        if refund_ratio > 0.4:
            score += 0.3
            reasons.append("High refund ratio")

    # 4️⃣ Yeni hesap riski
    account_age_days = (
        datetime.now(timezone.utc) - user["created_at"]
    ).days

    if account_age_days < 30:
        score += 0.2
        reasons.append("New account")

    # 5️⃣ VIP kullanıcılar için risk düşür
    if user["vip_tier"] in {"GOLD", "VIP"}:
        score -= 0.2
        reasons.append("VIP user")

    # Clamp
    score = max(0.0, min(score, 1.0))

    # Label
    if score < 0.3:
        label = "LOW"
    elif score < 0.7:
        label = "MEDIUM"
    else:
        label = "HIGH"

    return {
        "score": round(score, 2),
        "label": label,
        "reasons": reasons
    }

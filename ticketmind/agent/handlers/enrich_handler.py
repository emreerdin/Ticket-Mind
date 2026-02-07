from datetime import datetime, timezone
from ticketmind.agent.domain import risk
from ticketmind.db.repos import users_repo

def handle_enrich(context: dict):
    ticket = context["ticket"]
    user_id = ticket["user_id"]

    user = users_repo.get_user(user_id=user_id)
    if user is None:
        raise RuntimeError(f"User not found for user_id={user_id}")

    created_at = user["created_at"]
    now = datetime.now(timezone.utc)
    account_age_days = (now - created_at).days

    risk_result = risk.calculate_risk(user)

    context["user"] = {
        "id": user["user_id"],
        "account_age_days": account_age_days,
        "purchase_count": user["purchase_count"],
        "refund_count": user["refund_count"],
        "chargeback_count": user["chargeback_count"],
        "total_spent": float(user["total_spent"]),
        "vip_tier": user["vip_tier"],
        "locale": user["locale"],
    }

    context["risk"] = {
        "score": risk_result["score"],
        "label": risk_result["label"],
        "reasons": risk_result["reasons"],
    }

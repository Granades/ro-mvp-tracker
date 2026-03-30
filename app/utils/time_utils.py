from datetime import datetime, timezone

def format_time_until(dt):
    now = datetime.now(timezone.utc)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    diff = dt - now

    if diff.total_seconds() <= 0:
        return "ya salio"

    total = int(diff.total_seconds())
    hours = total // 3600
    minutes = (total % 3600) // 60

    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"
from datetime import datetime


def start_time_measuring() -> str:
    return datetime.utcnow().isoformat()


def get_total_time_measuring(start: str) -> float:
    return (datetime.utcnow() - datetime.fromisoformat(start)).total_seconds()

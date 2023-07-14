from datetime import datetime
import time

def start_time_measuring() -> str:
    return datetime.utcnow().isoformat()

def get_total_time_measuring(start) -> float:
    return (datetime.utcnow() - datetime.fromisoformat(start)).total_seconds()
import os

DEBUG = os.environ.get("debug") == "true"

REDIS_QUEUE_HOST = os.environ.get("REDIS_QUEUE_HOST", "localhost")
REDIS_RESULT_HOST = os.environ.get("REDIS_RESULT_HOST", "localhost")

REDIS_QUEUE_PASSWORD = os.environ.get("REDIS_QUEUE_PASSWORD", "")
REDIS_RESULT_PASSWORD = os.environ.get("REDIS_RESULT_PASSWORD", "")

REDIS_QUEUE_PORT = int(os.environ.get("REDIS_QUEUE_PORT", "6379"))
REDIS_RESULT_PORT = int(os.environ.get("REDIS_RESULT_PORT", "6379"))

INSTALLER_MAX_TASKS = int(os.environ.get("INSTALLER_MAX_TASKS", "26"))

REDIS_SECRET_KEY = os.environ.get(
    "REDIS_SECRET_KEY", "1InvkFDBGKDLpawxL6U2r0O4aVZJbPJI-XPwy7GudSs="
)

ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "")
ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "")

INSTALLER_IMAGE = os.environ.get(
    "image",
    "darkwind8/shapevpn:installer-latest",
)

REDIS_QUEUE = f"redis://:{REDIS_QUEUE_PASSWORD}@{REDIS_QUEUE_HOST}:{REDIS_QUEUE_PORT}/0"
REDIS_RESULT = (
    f"redis://:{REDIS_RESULT_PASSWORD}@{REDIS_RESULT_HOST}:{REDIS_RESULT_PORT}/0"
)

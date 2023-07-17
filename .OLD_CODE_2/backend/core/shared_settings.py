from dotenv import load_dotenv
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

REDIS_QUEUE_PORT = os.environ.get("REDIS_QUEUE_PORT", 6379)
REDIS_RESULT_PORT = os.environ.get("REDIS_RESULT_PORT", 6379)

INSTALLER_MAX_TASKS = int(os.environ.get("INSTALLER_MAX_TASKS", "26"))

FERNET_SECRET_KEY = os.environ["SECRET_KEY"].encode()

print(os.environ["SECRET_KEY"])
print(FERNET_SECRET_KEY)


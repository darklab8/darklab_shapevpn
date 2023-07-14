from pathlib import Path

from . import app
from .conftest import test_redis_host
from .interface import ui


def test_input_check() -> None:
    filepath = str(Path(__file__).parent.parent / "private.abc.key")
    with open(filepath, "r") as file:
        private_key = file.read()

    query = ui.UserInput(
        user="root",
        ip="shapevpn-installer-test-subject.light-search.com",
        auth_type="ssh",
        private_key=private_key,
        redis_host=test_redis_host,
        redis_port=6379,
        task_id=123,
        configs_encryption_key="1InvkFDBGKDLpawxL6U2r0O4aVZJbPJI-XPwy7GudSs=",
    )

    app.main([ui.Command.test_install.value] + query.to_args())

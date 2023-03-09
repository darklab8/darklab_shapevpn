import os

private_key_filename = "private.key"


def write_to_file(private_key: str) -> None:
    private_key = private_key.replace("\\n", "\n")

    if len(private_key) > 0:
        if private_key[-1] != "\n":
            private_key += "\n"

    with open(
        os.open(private_key_filename, os.O_CREAT | os.O_WRONLY, 0o600), "w"
    ) as file:
        file.write(private_key)

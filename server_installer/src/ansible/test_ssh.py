import pathlib
from . import ssh


def test_writing_file() -> None:
    assert True
    with open(str(pathlib.Path(__file__).parent / "testdata" / "testkey")) as file:
        data = file.read()

    private_key = data

    ssh.private_key_filename = "private.test.key"
    ssh.write_to_file(private_key)

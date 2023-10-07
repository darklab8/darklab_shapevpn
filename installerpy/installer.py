from pydantic import BaseModel
from . import types as t, capturer as c, storage as s


class InputData(BaseModel):
    port: t.ServerPort = t.ServerPort(22)
    key: t.SSHPrivateKeyPath
    host: t.ServerHostname
    user: t.ServerUser = t.ServerUser("root")


class Installer:
    def __init__(
            self,
            data: InputData,
            task_id: t.TaskID = t.TaskID("123"),
            task_name: t.TaskName = t.TaskName("abc"),
        ):
        self._data = data
        red = s.Redis()
        self._runner = c.Capturer(cmd=t.Command(f"""
ansible-playbook install_dockered_requirements.yml -i {str(self._data.host)}, --key-file {str(self._data.key)} -u {str(self._data.user)} --ssh-extra-args '-o ForwardAgent=yes' -e "ansible_port={str(self._data.port)}"
"""), task_id=task_id, task_name=task_name)
        self._runner.register_observer(red)

    def run(self) -> None:
        self._runner.run()

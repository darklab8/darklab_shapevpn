from .installer import Installer, InputData
from .settings import project_path
from installerpy.types import SSHPrivateKeyPath, ServerHostname, ServerUser
import logging
from . import log as l

logger = l.get_logger(__file__)

if __name__=="__main__":
    logger_root = logging.getLogger("")
    l.configure_logger(logger_root)

    logger.info("launching installer")
    Installer(data=InputData(
        key=SSHPrivateKeyPath(str((project_path / "id_rsa.test"))),
        host=ServerHostname("test.dd84ai.com"),
        user=ServerUser("root"),
    )).run()


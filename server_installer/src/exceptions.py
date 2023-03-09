class ServerInstallerException(Exception):
    pass


class RedisConnectionFaliure(ServerInstallerException):
    pass


class NotFound(ServerInstallerException):
    pass

from typing import Union

from cryptography.fernet import Fernet


# symetric encryptor
class ConfigEncryptor:
    def __init__(self, secret_key: Union[str, bytes]):
        self.secret_key = secret_key
        self.encryptor = Fernet(self.secret_key)

    @classmethod
    def generate_key(cls) -> bytes:
        return Fernet.generate_key()

    def encrypt_bytes(self, data: bytes) -> bytes:
        return self.encryptor.encrypt(data)

    def decrypt_bytes(self, data: bytes) -> bytes:
        return self.encryptor.decrypt(data)

    def encrypt_str(self, data: str) -> str:
        return (self.encrypt_bytes(data.encode())).decode()

    def decrypt_str(self, data: str) -> str:
        return (self.decrypt_bytes(data.encode())).decode()

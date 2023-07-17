from . import shared_settings
from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import base64
import os


class SymmetricEncryptor():

    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.encryptor = Fernet(self.secret_key)

    @classmethod
    def generate_key(cls):
        return Fernet.generate_key()

    def encrypt_bytes(self, data: bytes) -> bytes:
        return self.encryptor.encrypt(data)

    def decrypt_bytes(self, data: bytes) -> bytes:
        return self.encryptor.decrypt(data)

    def encrypt_str(self, data: str) -> str:
        return (self.encrypt_bytes(data.encode())).decode()

    def decrypt_str(self, data: str) -> str:
        return (self.decrypt_bytes(data.encode())).decode()

secret_encryptor = SymmetricEncryptor(shared_settings.FERNET_SECRET_KEY)

class SSHGenerator():

    @classmethod
    def generate(cls):
        key = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )

        private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        ).decode()

        public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        ).decode()
        return private_key, public_key


class AssymetricEncryptor():

    @classmethod
    def generate_keys(cls):
        key_ssh = rsa.generate_private_key(
            backend=crypto_default_backend(),
            public_exponent=65537,
            key_size=2048
        )

        private_key_ssh = key_ssh.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption()
        )

        public_key_ssh = key_ssh.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH
        )

        private_key_rsa = RSA.import_key(private_key_ssh)
        # public_key_rsa = private_key_rsa.publickey() # supposed to be needed for encryption, but in reality never needed :thinking:

        return private_key_ssh.decode(), public_key_ssh.decode()
    
    def __init__(self, private_key_ssh):
        self.private_key_rsa = RSA.import_key(private_key_ssh)
        self.public_key_rsa = self.private_key_rsa.publickey()

    def encrypt_str(self, data: str) -> str:
        cipher = PKCS1_OAEP.new(key=self.public_key_rsa)
        print(data)
        cipher_text = cipher.encrypt(data.encode())
        based = (base64.b64encode(cipher_text)).decode()
        print(based)
        return based

    def decrypt_str(self, data: str) -> str:
        decrypt = PKCS1_OAEP.new(key=self.private_key_rsa)
        decrypted_message = decrypt.decrypt(base64.b64decode(data))
        return decrypted_message.decode()

    @classmethod
    def write_to_file(cls, private_key):
        with open(os.open('private.key', os.O_CREAT | os.O_WRONLY, 0o600),'w' ) as file_:
            file_.write(private_key)

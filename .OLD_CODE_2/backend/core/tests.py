from dataclasses import dataclass
import subprocess
import logging
import docker
def test_check_capture():
    result = subprocess.run(
            [
                f'echo 123'
            ],
            capture_output=True,
            shell=True,
            text=True,
        )
    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.info(f"stdout={result.stdout}")
    logging.info(f"stderr={result.stderr}")

def test_make_command():
    a = (
        f'123'
        f' 456'
    )
    print(a)
    print(type(a))


from rest_framework import serializers
import rest_framework
import pytest

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

def test_using_valudator_with_error():
    serializer = CommentSerializer(data={"some": "data"})
    with pytest.raises(rest_framework.exceptions.ValidationError):
        serializer.is_valid(raise_exception=True)

class CommentSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)
    page = serializers.IntegerField(min_value=1, default=1)


class Query(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, default=1)
    page_size = serializers.IntegerField(min_value=1, max_value=1000, default=100)

def test_using_valudator_correctly():
    serializer = CommentSerializer(data={"content": "data"})
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    assert serializer.validated_data["content"] == "data"
    assert serializer.validated_data["page"] == 1
        
def test_using_valudator_with_extra_data():
    serializer = CommentSerializer(data={"content": "data", "123": "456"})
    serializer.is_valid(raise_exception=True)


# def test_launching_container():
#     client = docker.from_env()

#     try:
#         result = client.containers.run("ubuntu", "/bin/bash -c -- 'mkdir 1/2/3/4/5'", environment={
#             "ABC": "123"
#         })
#     except docker.errors.ContainerError as error:
#         error_happened=True
#         print(error)

#     assert error_happened
#     print(123)

# import re
# def test_launching_container():
#     client = docker.from_env()

#     try:
#         container = client.containers.run("registry.gitlab.com/gtn_admins/constructor/constructor_server_installer/constructor-installer:dev", 
#         environment={
#             "ip": "134.209.30.119",
#             "user": "root",
#             "auth": "ssh"
#         },
#         detach=True
#         )

#         log_stream = container.logs(stream=True)
#         for log_record in log_stream:
#             decoded_log_string = log_record.decode("utf-8") 

#             if decoded_log_string == '\n':
#                 continue

#             task_record = re.search('=TASK \[(.+)\].[*]+', decoded_log_string)
#             if task_record is None:
#                 continue

#             print(task_record.group(1))

#         print("finished")
            

#     except docker.errors.ContainerError as error:
#         error_happened=True
#         print("docker.errors.ContainerError, stderr={error}")

def test_fernet():
    from core.encryptor import secret_encryptor
    data = "my deep dark secret"
    encrypted = secret_encryptor.encrypt_str(data)

    assert encrypted != data

    decrypted = secret_encryptor.decrypt_str(encrypted)
    
    assert decrypted == data
    
def test_rsa():
    #RSA_cryptography.py
    #Importing necessary modules
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from binascii import hexlify

    #The message to be encrypted
    message = b'Public and Private keys encryption'

    #Generating private key (RsaKey object) of key length of 1024 bits
    private_key = RSA.generate(4096)

    #Generating the public key (RsaKey object) from the private key
    public_key = private_key.publickey()
    print(type(private_key), type(public_key))

    #Converting the RsaKey objects to string 
    private_pem = private_key.export_key().decode()
    public_pem = public_key.export_key().decode()
    print(type(private_pem), type(public_pem))
    #Writing down the private and public keys to 'pem' files
    with open('private_pem.pem', 'w') as pr:
        pr.write(private_pem)
    with open('public_pem.pem', 'w') as pu:
        pu.write(public_pem)

    #Importing keys from files, converting it into the RsaKey object   
    pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
    pu_key = RSA.import_key(open('public_pem.pem', 'r').read())

    print(type(pr_key), type(pu_key))
    #Instantiating PKCS1_OAEP object with the public key for encryption
    cipher = PKCS1_OAEP.new(key=pu_key)
    #Encrypting the message with the PKCS1_OAEP object
    cipher_text = cipher.encrypt(message)
    print(cipher_text)
    #Instantiating PKCS1_OAEP object with the private key for decryption
    decrypt = PKCS1_OAEP.new(key=pr_key)
    #Decrypting the message with the PKCS1_OAEP object
    decrypted_message = decrypt.decrypt(cipher_text)
    print(decrypted_message)

    public_key.export_key("OpenSSH").decode()

def test_ssh_key_pair():
    from cryptography.hazmat.primitives import serialization as crypto_serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.backends import default_backend as crypto_default_backend

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


    #RSA_cryptography.py
    #Importing necessary modules
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA
    from binascii import hexlify

    #The message to be encrypted
    message = b'Public and Private keys encryption'

    #Generating private key (RsaKey object) of key length of 1024 bits
    private_key = RSA.import_key(private_key_ssh)

    #Generating the public key (RsaKey object) from the private key
    public_key = private_key.publickey()
    print(type(private_key), type(public_key))

    #Converting the RsaKey objects to string 
    private_pem = private_key.export_key().decode()
    public_pem = public_key.export_key().decode()
    print(type(private_pem), type(public_pem))
    #Writing down the private and public keys to 'pem' files
    with open('private_pem.pem', 'w') as pr:
        pr.write(private_pem)
    with open('public_pem.pem', 'w') as pu:
        pu.write(public_pem)

    #Importing keys from files, converting it into the RsaKey object   
    pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
    pu_key = RSA.import_key(open('public_pem.pem', 'r').read())

    print(type(pr_key), type(pu_key))
    #Instantiating PKCS1_OAEP object with the public key for encryption
    cipher = PKCS1_OAEP.new(key=pu_key)
    #Encrypting the message with the PKCS1_OAEP object
    cipher_text = cipher.encrypt(message)
    print(cipher_text)
    #Instantiating PKCS1_OAEP object with the private key for decryption
    decrypt = PKCS1_OAEP.new(key=pr_key)
    #Decrypting the message with the PKCS1_OAEP object
    decrypted_message = decrypt.decrypt(cipher_text)
    print(decrypted_message)

def test_assymetric_encryptor():
    from .encryptor import AssymetricEncryptor

    private, public = AssymetricEncryptor.generate_keys()

    encryptor = AssymetricEncryptor(private)

    data = "random text"

    encrypted = encryptor.encrypt_str(data)

    assert data != encrypted

    decrypted = encryptor.decrypt_str(encrypted)

    assert data == decrypted
    print(decrypted)

def test_assymetric_encryptor():
    from .encryptor import AssymetricEncryptor

    private_key, public_key = AssymetricEncryptor.generate_keys()

    print(private_key)
    print(public_key)

    AssymetricEncryptor.write_to_file(private_key)
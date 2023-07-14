from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
print(key.decode())
print(key.decode().encode())
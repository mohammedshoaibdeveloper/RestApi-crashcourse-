import hashlib
import os

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    salt_hex = salt.hex()
    pwd_hash = hashlib.md5((password + salt_hex).encode('utf-8')).hexdigest()
    return (salt_hex + pwd_hash).encode('utf-8')

def check_password(password, hashed_password):
    salt_hex = hashed_password[:32]
    salt = bytes.fromhex(salt_hex)
    hashed_password_check = hash_password(password, salt)
    return hashed_password_check.decode() == hashed_password







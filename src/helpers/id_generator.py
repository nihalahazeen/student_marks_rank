import hashlib

def generate_hash(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()
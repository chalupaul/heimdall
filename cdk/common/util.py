import hashlib

def build_deps():
    contents = open("poetry.lock", 'rb').read()
    existing_checksum = hashlib.md5(contents).hexdigest()
    print(existing_checksum)
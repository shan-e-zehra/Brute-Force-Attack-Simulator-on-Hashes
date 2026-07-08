import hashlib

def generate_hash(password, algorithm="md5", salt=""):
    combined = password + salt
    if algorithm == "md5":
        return hashlib.md5(combined.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(combined.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm")

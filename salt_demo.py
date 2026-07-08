from hash_utils import generate_hash

def salt_demo(password):
    salt = "X9@!"
    print("\n--- SALT DEMO ---")
    print("Without Salt:", generate_hash(password, "sha256"))
    print("With Salt   :", generate_hash(password, "sha256", salt))

from hash_utils import generate_hash
from dictionary_attack import dictionary_attack
from brute_force import brute_force_attack
from salt_demo import salt_demo

print("=== Brute Force Attack Simulator ===")

password = input("Enter password: ")
algorithm = input("Hash (md5/sha256): ").lower()
use_salt = input("Use salt? (yes/no): ").lower()

salt = "X9@!" if use_salt == "yes" else ""

hashed = generate_hash(password, algorithm, salt)
print("\nStored Hash:", hashed)

attack = input("Attack (dictionary/brute): ").lower()

if attack == "dictionary":
    result, t = dictionary_attack(hashed, algorithm, salt)
elif attack == "brute":
    result, t = brute_force_attack(hashed, algorithm, salt)
else:
    print("Invalid choice")
    exit()

if result:
    print("\nPassword Cracked:", result)
    print("Time:", round(t, 2), "sec")
else:
    print("\nPassword NOT cracked")

salt_demo(password)

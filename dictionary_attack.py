import time
from hash_utils import generate_hash

def dictionary_attack(target_hash, algorithm, salt=""):
    start = time.time()

    with open("wordlist.txt", "r") as file:
        for word in file:
            word = word.strip()
            if generate_hash(word, algorithm, salt) == target_hash:
                return word, time.time() - start

    return None, None

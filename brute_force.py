import itertools
import string
import time
from hash_utils import generate_hash

def brute_force_attack(target_hash, algorithm, salt="", max_length=4):
    chars = string.ascii_lowercase + string.digits
    start = time.time()

    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            attempt = ''.join(combo)
            if generate_hash(attempt, algorithm, salt) == target_hash:
                return attempt, time.time() - start

    return None, None

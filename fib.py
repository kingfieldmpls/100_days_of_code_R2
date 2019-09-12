from functools import lru_cache


def fib(n):
    print(f"Calling fib with {n}")
    if n < 2:
        print(f"Returning {n}")
        return n
    return fib(n - 2) + fib(n - 1)


fibs = {0: 0, 1: 1}


def fib1(n):
    if n not in fibs:
        fibs[n] = fib1(n - 2) + fib1(n - 1)
    return fibs[n]


@lru_cache(maxsize=None)
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)


from secrets import token_bytes


def random_key(length):
    tb = token_bytes(length)
    print(len(tb))
    print(tb)
    return int.from_bytes(tb, "big")


def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1, key2):
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

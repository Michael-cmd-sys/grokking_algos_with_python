from typing import Callable

def interpret_prime_result(func: Callable[[int], int]):
    def wrapper(arg: int):
        result = func(arg)
        if result:
            return f"{arg} is prime"
        else:
            return f"{arg} is not prime"

    return wrapper

@interpret_prime_result
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    nums = range(2, (num // 2))
    for factor in nums:
        if num % factor == 0:
            return False

    return True

print(is_prime(15))
print(is_prime(2))
print(is_prime(23))

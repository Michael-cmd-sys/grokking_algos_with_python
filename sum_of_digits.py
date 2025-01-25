from time import time
from typing import Callable

def func_details(func: Callable[[int], int]):
    def wrapper(arg):
        init_time = time()
        result = func(arg)
        total_time = time() - init_time
        if result:
            return f"Sum of digits = {result} completed in {total_time:.4f}ms"

    return wrapper

@func_details
def compute_sum_of_digits(num: int) -> int:
    num = abs(num)
    total = 0 

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    return total

print(compute_sum_of_digits(12345))
print(compute_sum_of_digits(2025))
print(compute_sum_of_digits(-2048))

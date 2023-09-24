import time
import random


def is_prime_v1(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime_v2(number: int) -> bool:
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_prime_v3(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def is_prime_v4(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, int(number ** 0.5) + 1, 6):
        if number % i == 0 or number % (i+2) == 0:
            return False
    return True


if __name__ == '__main__':

    numbers = [random.randint(0, 1000) for _ in range(100000)]

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print('v3', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v4(num)
    print('v4', time.time() - start)

import time


def memorize(func):
    cache = {}

    def _wrapper(num):
        if num not in cache:
            cache[num] = func(num)
        return cache[num]
    return _wrapper


@memorize
def long_func(num: int) -> int:
    result = 0
    for i in range(10000000):
        result += num*i
    return result


if __name__ == "__main__":
    for i in range(10):
        print(long_func(i))

    start = time.time()
    for i in range(10):
        print(long_func(i))
    end = time.time()
    print(f"long_func: {end-start}")

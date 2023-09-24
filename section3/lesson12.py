from random import randint
from lesson11 import insertion_sort


def bucket_sort(numbers: list[int]) -> list[int]:
    max_number = max(numbers)
    length = len(numbers)
    size = max_number // length

    buckets = [[] for _ in range(size)]
    for number in numbers:
        i = number // size
        if i != size:
            buckets[i].append(number)
        else:
            buckets[size-1].append(number)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]
    return result


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(bucket_sort(numbers))

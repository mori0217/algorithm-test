from random import randint


def counting_sort(numbers: list[int], place: int):
    COUNT_SIZE = 10
    counts = [0] * COUNT_SIZE
    result = [0] * len(numbers)

    for number in numbers:
        index = int(number / place) % COUNT_SIZE
        counts[index] += 1

    for i in range(1, COUNT_SIZE):
        counts[i] += counts[i-1]

    i = len(numbers)-1
    while i >= 0:
        index = int(numbers[i]/place) % COUNT_SIZE
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


def radix_sort(numbers: list[int]):
    max_number = max(numbers)
    place = 1
    while max_number > place:
        numbers = counting_sort(numbers, place)
        place *= 10
    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(radix_sort(numbers))

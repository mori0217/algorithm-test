from random import randint


def counting_sort(numbers: list[int]):
    max_number = max(numbers)
    counts = [0 for _ in range(max_number+1)]
    result = [0 for _ in range(len(numbers))]

    for number in numbers:
        counts[number] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers)-1
    while i >= 0:
        index = numbers[i]
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(counting_sort(numbers))

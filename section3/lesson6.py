import random


def bubble_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == "__main__":
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(bubble_sort(numbers))

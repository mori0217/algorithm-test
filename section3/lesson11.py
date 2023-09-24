from random import randint


def insertion_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(1, length):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(insertion_sort(numbers))

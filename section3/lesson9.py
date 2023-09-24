from random import randint


def selection_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(selection_sort(numbers))

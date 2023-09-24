import random


def cocktail_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    swapped = True
    start = 0
    end = length - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break

        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


if __name__ == "__main__":
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(cocktail_sort(numbers))

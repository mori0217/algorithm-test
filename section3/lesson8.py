import random


def comb_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    gap = length
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap/1.3)
        if gap < 1:
            gap = 1

        swapped = False
        for i in range(0, length-gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i+gap] = numbers[i+gap], numbers[i]
                swapped = True
    return numbers


if __name__ == "__main__":
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(comb_sort(numbers))

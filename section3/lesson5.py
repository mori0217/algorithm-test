import random


def in_order(numbers: list[int]) -> bool:
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True
    return all([numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)])


def bogo_sort(numbers: list[int]) -> list[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(bogo_sort(numbers))

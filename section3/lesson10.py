from random import randint


def gnome_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    index = 0
    while index < length:
        if index == 0:
            index += 1
        if numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1
    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(gnome_sort(numbers))

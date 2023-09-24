from random import randint


def shell_sort(numbers: list[int]):
    length = len(numbers)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(shell_sort(numbers))

def delete_duplicate_v1(numbers: list[int]) -> None:
    temp = []
    for num in numbers:
        if num not in temp:
            temp.append(num)
    numbers[:] = temp


def delete_duplicate_v2(numbers: list[int]) -> None:
    temp = [numbers[0]]
    index = 0
    len_numbers = len(numbers) - 1
    while index < len_numbers:
        if numbers[index] != numbers[index + 1]:
            temp.append(numbers[index + 1])
        index += 1
    numbers[:] = temp


def delete_duplicate_v3(numbers: list[int]) -> None:
    index = 0
    while index < len(numbers) - 1:
        if numbers[index] == numbers[index + 1]:
            numbers.remove(numbers[index])
            index -= 1
        index += 1


def delete_duplicate_v4(numbers: list[int]) -> None:
    index = len(numbers) - 1
    while index > 0:
        if numbers[index] == numbers[index - 1]:
            numbers.pop(index)
        index -= 1


if __name__ == '__main__':
    input = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    delete_duplicate_v1(input)
    print(input)

    input = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    delete_duplicate_v2(input)
    print(input)

    input = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    delete_duplicate_v3(input)
    print(input)

    input = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    delete_duplicate_v4(input)
    print(input)

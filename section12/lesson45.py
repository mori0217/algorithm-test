def remove_zero(numbers: list[int]) -> None:
    if not numbers:
        return
    if numbers[0] != 0:
        return
    numbers.pop(0)
    remove_zero(numbers)


def list_to_int(numbers: list[int]) -> int:
    if not numbers:
        return 0
    sum = 0
    for i, num in enumerate(numbers[::-1]):
        sum += num * (10**i)
    return sum


def list_to_int_plus_one(numbers: list[int]) -> int:
    index = len(numbers) - 1
    numbers[index] += 1
    while index > 0:
        if numbers[index] != 10:
            remove_zero(numbers)
            break
        numbers[index] = 0
        numbers[index - 1] += 1
        index -= 1
    if numbers[0] == 10:
        numbers[0] = 1
        numbers.append(0)
    return list_to_int(numbers)


if __name__ == '__main__':
    print(list_to_int_plus_one([1]))
    print(list_to_int_plus_one([2, 3]))
    print(list_to_int_plus_one([8, 9]))
    print(list_to_int_plus_one([9, 9]))
    print(list_to_int_plus_one([1, 2, 3]))
    print(list_to_int_plus_one([7, 8, 9]))
    print(list_to_int_plus_one([9, 9, 9]))
    print(list_to_int_plus_one([0, 0, 0, 9, 9, 9, 9, 9, 9]))

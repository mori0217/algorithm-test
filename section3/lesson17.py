from random import randint


def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_index = 0
    right_index = 0
    numbers_index = 0

    length_left = len(left)
    length_right = len(right)

    while left_index < length_left and right_index < length_right:
        if left[left_index] <= right[right_index]:
            numbers[numbers_index] = left[left_index]
            left_index += 1
        else:
            numbers[numbers_index] = right[right_index]
            right_index += 1
        numbers_index += 1

    while left_index < length_left:
        numbers[numbers_index] = left[left_index]
        left_index += 1
        numbers_index += 1

    while right_index < length_right:
        numbers[numbers_index] = right[right_index]
        right_index += 1
        numbers_index += 1

    return numbers


if __name__ == "__main__":
    numbers = [randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(merge_sort(numbers))

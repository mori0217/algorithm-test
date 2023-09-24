from random import randint
from typing import NewType

IndexNumber = NewType('IndexNumber', int)


def linear_search(numbers: list[int], value: int) -> IndexNumber:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return IndexNumber(i)
    return IndexNumber(-1)


def binary_search(numbers: list[int], value:  int) -> IndexNumber:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return IndexNumber(mid)
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return IndexNumber(-1)


def binary_search_recursive(numbers: list[int], value: int) -> IndexNumber:
    def _binary_search_recursive(numbers: list[int], value, left: int, right: int) -> IndexNumber:
        if left > right:
            return IndexNumber(-1)
        mid = (left + right) // 2
        if numbers[mid] == value:
            return IndexNumber(mid)
        elif numbers[mid] < value:
            return _binary_search_recursive(numbers, value, mid+1, right)
        else:
            return _binary_search_recursive(numbers, value, left, mid - 1)
    return _binary_search_recursive(numbers, value, 0, len(numbers) - 1)


if __name__ == "__main__":
    nums = [randint(0, 1000) for _ in range(10)]
    nums.sort()
    value = nums[randint(0, len(nums) - 1)]
    print(nums)
    print(value)
    print(linear_search(nums, value))
    print(binary_search(nums, value))
    print(binary_search_recursive(nums, value))

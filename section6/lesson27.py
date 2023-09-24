

def get_pair(numbers: list[int], target: int) -> tuple[int, int] | None:
    cache = set()
    for num in numbers:
        value = target - num
        if value in cache:
            return num, value
        cache.add(num)


def get_pair_half_sum(numbers: list[int]) -> tuple[int, int] | None:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return None
    # half_sum = sum_numbers // 2
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return None

    cache = set()
    for num in numbers:
        value = half_sum - num
        if value in cache:
            return value, num
        cache.add(num)


if __name__ == '__main__':
    input = [11, 2, 5, 9, 10, 3]
    target = 12
    print(get_pair(input, target))

    input = [11, 2, 5, 9, 10, 3]
    print(get_pair_half_sum(input))

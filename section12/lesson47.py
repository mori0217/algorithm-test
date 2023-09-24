def get_max_min_sequence_sum(numbers: list[int], operator=max) -> int:
    result = 0
    sum = 0
    for num in numbers:
        sum = operator(sum + num, num)
        result = operator(result, sum)
    #     temp_sum = sum + num
    #     if temp_sum > num:
    #         sum = temp_sum
    #     else:
    #         sum = num
    #     if result < sum:
    #         result = sum
    return result


def find_max_circular_sequence_sum(numbers: list[int]) -> int:
    max_invert_numbers = get_max_min_sequence_sum(numbers)
    max_wrap_sequence = sum(numbers) - get_max_min_sequence_sum(numbers, operator=min)
    # all_sum = 0
    # invert_numbers = []
    # for num in numbers:
    #     all_sum += num
    #     invert_numbers.append(-num)
    # max_invert_numbers = get_max_min_sequence_sum(invert_numbers)
    # max_wrap_sequence = all_sum - (-max_invert_numbers)
    return max(max_invert_numbers, max_wrap_sequence)


if __name__ == '__main__':
    l = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_max_min_sequence_sum(l))
    print(find_max_circular_sequence_sum(l))

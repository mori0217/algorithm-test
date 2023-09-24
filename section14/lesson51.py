def order_even_first_odd_last_v1(numbers: list[int]) -> None:
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    numbers[:] = even_list + odd_list


def order_even_first_odd_last_v2(numbers: list[int]) -> None:
    start = 0
    end = len(numbers) - 1
    while start < end:
        if numbers[start] % 2 == 0:
            start += 1
        else:
            numbers[start], numbers[end] = numbers[end], numbers[start]
            end -= 1
        print(numbers)


if __name__ == '__main__':
    l = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    order_even_first_odd_last_v1(l)
    l = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    order_even_first_odd_last_v2(l)
    print(l)

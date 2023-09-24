def order_change_by_indexes_v1(chars: list[str], indexes: list[int]) -> str:
    tmp = [None] * len(chars)
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return "".join(tmp)


def order_change_by_indexes_v2(chars: list[str], indexes: list[int]) -> str:
    i = 0
    length = len(indexes) - 1
    while i < length:
        while i != indexes[i]:
            index = indexes[i]
            chars[i], chars[index] = chars[index], chars[i]
            indexes[i], indexes[index] = indexes[index], indexes[i]
        i += 1
    return "".join(chars)


if __name__ == '__main__':
    w = ['h', 'y', 'n', 'p', 't', 'o']
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_by_indexes_v1(w, i))

    w = ['h', 'y', 'n', 'p', 't', 'o']
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_by_indexes_v2(w, i))

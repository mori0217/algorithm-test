import operator


def snake_string_v1(chars: str) -> list[list[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for index, char in enumerate(chars):
        if index % 4 == 1:
            insert_index = 0
        elif index % 2 == 0:
            insert_index = 1
        elif index % 4 == 3:
            insert_index = 2
        result[insert_index].append(char)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


def snake_string_v2(chars: str, depth: int) -> list[list[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = depth // 2

    op = operator.neg
    for char in chars:
        result[insert_index].append(char)
        for rest_idex in result_indexes - {insert_index}:
            result[rest_idex].append(" ")
        if insert_index <= 0:
            op = operator.pos
        elif insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)

    return result


if __name__ == '__main__':
    numbers = [str(i) for j in range(5) for i in range(10)]
    strings = "".join(numbers)
    for line in snake_string_v1(strings):
        print("".join(line))

    alphabet = [s for _ in range(5) for s in "abcdefghijklmnopqrstuvwxyz"]
    strings = "".join(alphabet)
    for line in snake_string_v2(strings, 10):
        print("".join(line))

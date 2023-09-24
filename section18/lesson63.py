import random


def generate_triangle_list(depth: int, max_num: int) -> list[list[int]]:
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth+1)]


def print_triangle(data: list[list[int]]) -> None:
    max_data_list = [max(line) for line in data]
    max_data = max(max_data_list)
    max_length = len(str(max_data))
    width = max_length + (max_length % 2) + 2
    for index, line in enumerate(data):
        centered_line_list = [str(item).center(width, " ") for item in line]
        centered_line = "".join(centered_line_list)
        left_padding = " " * int(width/2) * (len(data) - index)
        print(left_padding, centered_line)


def sum_min_path(data: list[list[int]]) -> int | None:
    tree_sum = data[:]
    line_index = 1
    line_length = len(data)
    while line_index < line_length:
        line = data[line_index]
        line_path_sum = []
        for index, item in enumerate(line):
            before_line = tree_sum[line_index-1]
            if index == 0:
                value = item + before_line[0]
            elif index == len(line) - 1:
                value = item + before_line[index-1]
            else:
                min_path = min(before_line[index-1], before_line[index])
                value = item + min_path
            line_path_sum.append(value)
        tree_sum[line_index] = line_path_sum
        line_index += 1
    return min(tree_sum[-1])


if __name__ == '__main__':
    data = generate_triangle_list(5, 9)
    print(data)
    print_triangle(data)
    print(sum_min_path(data))

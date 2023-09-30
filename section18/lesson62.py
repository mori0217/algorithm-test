def generate_pascal_triangle(depth: int) -> list[list[int]]:
    data = [[1] * (i+1) for i in range(depth)]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line-1][i-1]+data[line-1][i]
    return data


def print_pascal(data: list[list[int]]) -> None:
    max_length = len(str(max(data[-1])))
    width = max_length + (max_length % 2) + 2
    for index, line in enumerate(data):
        centered_line_list = [str(index).center(width, "*") for index in line]
        centered_line = "".join(centered_line_list)
        # print(centered_line)
        left_space = " " * int((width/2) * (len(data) - index))
        print(left_space, centered_line)


if __name__ == '__main__':
    print_pascal(generate_pascal_triangle(3))

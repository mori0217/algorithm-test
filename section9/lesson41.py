
def find_pair(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    cache = {}
    result = []
    for pair in pairs:
        first, second = pair
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            result.append(pair)
    return result


if __name__ == "__main__":
    input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    for pair in find_pair(input):
        print(pair)


from collections import Counter


def count_chars_v1(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    count_list = []
    # for char in strings:
    #     if not char.isspace():
    #         count_list.append((char, strings.count(char)))
    count_list = [(char, strings.count(char)) for char in strings if not char.isspace()]
    return max(count_list, key=lambda x: x[1])


def count_chars_v2(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    count_dict = {}
    for char in strings:
        if not char.isspace():
            count_dict[char] = count_dict.get(char, 0) + 1
    max_key = max(count_dict, key=lambda x: count_dict[x])
    return (max_key, count_dict[max_key])


def count_chars_v3(strings: str) -> tuple[str, int]:
    strings = strings.lower()
    counter = Counter()
    for char in strings:
        if not char.isspace():
            counter[char] += 1
    return counter.most_common(1)[0]


if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(s))
    print(count_chars_v2(s))
    print(count_chars_v3(s))

NUM_ALPHABET_MAPPING = {
    0: "+",
    1: "@",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WSYZ"
}


def phone_mnemonic_v1(phone_number: str) -> list[str]:
    phone_number = [int(s) for s in phone_number.replace("-", "")]
    result = []
    tmp = [""] * len(phone_number)

    def find_candidate(index: int = 0) -> None:
        if index == len(phone_number):
            result.append("".join(tmp))
            return
        for char in NUM_ALPHABET_MAPPING[phone_number[index]]:
            tmp[index] = char
            find_candidate(index + 1)
    find_candidate()
    return result


def phone_mnemonic_v2(phone_number: str) -> list[str]:
    phone_number = [int(s) for s in phone_number.replace("-", "")]
    result = []
    stack = [""]

    while len(stack) != 0:
        value = stack.pop()
        if len(value) == len(phone_number):
            result.append(value)
            continue
        for char in NUM_ALPHABET_MAPPING[phone_number[len(value)]]:
            stack.append(value + char)
    return result


if __name__ == '__main__':
    for s in phone_mnemonic_v2('23'):
        print(s)

    for s in phone_mnemonic_v1('568-379-8466'):
        if 'LOVEPYTHON' in s:
            print(s)

    for s in phone_mnemonic_v2('568-379-8466'):
        if 'LOVEPYTHON' in s:
            print(s)

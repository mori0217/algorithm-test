import json


def validate_format(chars: str) -> bool:
    lookup = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    stack = []
    for char in chars:
        if char in lookup:
            stack.append(lookup[char])
        elif char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    print(validate_format("(){}[]"))
    print(validate_format("()[{)}"))
    print(validate_format("()[{}]"))
    d = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}
    print(validate_format(json.dumps(d)))

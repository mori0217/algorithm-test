from typing import Generator


def is_palindrome(strings: str) -> bool:
    length = len(strings)
    if not length:
        return False
    if length == 1:
        return True
    start = 0
    end = length - 1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


def find_palindrome(strings: str, left: int, right: int) -> Generator[str, None, None]:
    while left >= 0 and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        yield strings[left:right+1]
        left -= 1
        right += 1


def find_all_palindrome(strings: str) -> Generator[str, None, None]:
    length = len(strings)
    if not length:
        yield ""
    if length == 1:
        yield strings

    for i in range(1, length - 1):
        yield from find_palindrome(strings, i-1, i+1)
        yield from find_palindrome(strings, i, i+1)


if __name__ == "__main__":
    print(is_palindrome("tacocat"))
    print(is_palindrome("tacocats"))
    for s in find_all_palindrome("tacocat"):
        print(s)
    for s in find_all_palindrome("fdafiewaafcabacdfafdaf"):
        print(s)

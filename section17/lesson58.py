
# import string
from typing import Generator


def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    # len_alphabet = len(string.ascii_uppercase)
    len_alphabet = ord("Z") - ord("A") + 1

    for char in text:
        # if char.isupper():
        #     alphabet = string.ascii_uppercase
        # elif char.islower():
        #     alphabet = string.ascii_lowercase
        # else:
        #     result += char
        #     continue

        # index = (alphabet.index(char) + shift) % len_alphabet
        # result += alphabet[index]

        if char.isupper():
            char_index = (ord(char) + shift - ord("A")) % len_alphabet + ord("A")
        elif char.islower():
            char_index = (ord(char) + shift - ord("a")) % len_alphabet + ord("a")
        else:
            result += char
            continue
        result += chr(char_index)

    return result


def caesar_cipher_hack(text: str) -> Generator[tuple[int, str], None, None]:
    # len_alphabet = len(string.ascii_uppercase)
    len_alphabet = ord("Z") - ord("A") + 1

    for candidate_shift in range(1, len_alphabet+1):
        reversed = ""
        for char in text:
            # if char.isupper():
            #     alphabet = string.ascii_uppercase
            # elif char.islower():
            #     alphabet = string.ascii_lowercase
            # else:
            #     reversed += char
            #     continue

            # index = alphabet.index(char) - candidate_shift
            # if index < 0:
            #     index += len_alphabet
            # reversed += alphabet[index]

            if char.isupper():
                start_index = ord("A")
            elif char.islower():
                start_index = ord("a")
            else:
                reversed += char
                continue

            index = ord(char) - candidate_shift
            if index < start_index:
                index += len_alphabet
                reversed += chr(index)

        yield candidate_shift, reversed


if __name__ == '__main__':
    s = -3
    encrypted = caesar_cipher("HELLO world", s)
    print(encrypted)
    print(caesar_cipher(encrypted, -s))
    for shift_num, decrypted in caesar_cipher_hack(encrypted):
        print(f'{shift_num:2d}', decrypted)

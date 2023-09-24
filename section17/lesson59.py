ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LEN_ALPHABET = len(ALPHABET)


def generate_key(message: str, keyword: str) -> str:
    result = keyword
    keyword_length = len(keyword)
    remain_length = len(message) - keyword_length
    for i in range(remain_length):
        result += keyword[i % keyword_length]
    return result


def encrypt(message: str, key: str) -> str:
    result = ""
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue
        # char_index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % LEN_ALPHABET
        # result += ALPHABET[char_index]
        char_index = (ord(char) + ord(key[i])) % LEN_ALPHABET + ord("A")
        result += chr(char_index)

    return result


def decrypt(message: str, key: str) -> str:
    result = ""
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue
        # char_index = (ALPHABET.index(char) - ALPHABET.index(key[i]) + LEN_ALPHABET) % LEN_ALPHABET
        # result += ALPHABET[char_index]
        char_index = (ord(char) - ord(key[i]) + LEN_ALPHABET) % LEN_ALPHABET + ord("A")
        result += chr(char_index)
    return result


if __name__ == '__main__':
    t = 'HELLO WORLD'
    k = generate_key(t, 'CAT')
    print(k)
    e = encrypt(t, k)
    print(e)
    d = decrypt(e, k)
    print(d)

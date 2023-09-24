from dataclasses import dataclass
import random


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@dataclass
class PlugBoard:
    forward_map: dict[str, str]
    backward_map: dict[str, str]
    alphabet: str = ALPHABET

    def __init__(self, map_alphabet: str) -> None:
        self.forward_map = {}
        self.backward_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet: str) -> None:
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        self.backward_map = dict(zip(map_alphabet, self.alphabet))

    def forward(self, index_number: int) -> int:
        char = self.alphabet[index_number]
        char = self.forward_map[char]
        return self.alphabet.index(char)

    def backward(self, index_number: int) -> int:
        char = self.alphabet[index_number]
        char = self.backward_map[char]
        return self.alphabet.index(char)


@dataclass
class Rotor(PlugBoard):
    offset: int = 0
    rotations = 0

    def __init__(self, map_alphabet: str, offset: int = 0) -> None:
        super().__init__(map_alphabet)
        self.offset = offset

    def rotate(self, offset: int | None = None) -> int:
        if offset is None:
            offset = self.offset
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        return self.rotations

    def reset(self) -> None:
        self.rotations = 0
        self.alphabet = ALPHABET


@dataclass
class Reflector:
    reflect_map: dict[str, str]

    def __init__(self, map_alphabet: str) -> None:
        self.reflect_map = dict(zip(ALPHABET, map_alphabet))
        for x, y in self.reflect_map.items():
            if x != self.reflect_map[y]:
                raise ValueError(x, y, "is not a valid reflector map")

    def reflect(self, index_number: int) -> int:
        char = ALPHABET[index_number]
        char = self.reflect_map[char]
        return ALPHABET.index(char)


@dataclass
class EnigmaMachine:
    plugboard: PlugBoard
    rotors: list[Rotor]
    reflector: Reflector

    def __init__(self, plugboard: PlugBoard, rotors: list[Rotor], reflector: Reflector) -> None:
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, message: str) -> str:
        return "".join([self.go_through(char) for char in message])

    def decrypt(self, message: str) -> str:
        for rotor in self.rotors:
            rotor.reset()
        return "".join([self.go_through(char) for char in message])

    def go_through(self, char: str) -> str:
        char = char.upper()
        if char not in ALPHABET:
            return char
        index = ALPHABET.index(char)
        index = self.plugboard.forward(index)

        for rotor in self.rotors:
            index = rotor.forward(index)

        index = self.reflector.reflect(index)

        for rotor in reversed(self.rotors):
            index = rotor.backward(index)

        index = self.plugboard.backward(index)

        char = ALPHABET[index]

        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return char


if __name__ == "__main__":
    def get_random_alphabet(): return "".join(random.sample(ALPHABET, len(ALPHABET)))
    plugboard = PlugBoard(get_random_alphabet())
    rotor1 = Rotor(get_random_alphabet(), 3)
    rotor2 = Rotor(get_random_alphabet(), 5)
    rotor3 = Rotor(get_random_alphabet(), 7)

    reflect_alphabet = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes)/2)):
        x = indexes.pop(random.randint(0, len(indexes)-1))
        y = indexes.pop(random.randint(0, len(indexes)-1))
        reflect_alphabet[x], reflect_alphabet[y] = reflect_alphabet[y], reflect_alphabet[x]
    reflect_alphabet = "".join(reflect_alphabet)
    reflector = Reflector(reflect_alphabet)

    enigma_machine = EnigmaMachine(
        plugboard,
        [rotor1, rotor2, rotor3],
        reflector
    )
    message = "Hello World"
    encrypted = enigma_machine.encrypt(message)
    print(encrypted)
    decrypted = enigma_machine.decrypt(encrypted)
    print(decrypted)

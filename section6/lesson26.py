import hashlib
from dataclasses import dataclass
from typing import Any


@dataclass
class HashTable:
    size: int
    table: list[list[tuple[str, Any]]]

    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [[] for _ in (range(self.size))]

    def _hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: str, value: Any) -> None:
        index = self._hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data = (key, value)
                break
        else:
            self.table[index].append((key, value))

    def get(self, key: str) -> Any:
        index = self._hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        return None

    def __setitem__(self, key: str, value: Any) -> None:
        self.add(key, value)

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")
            print()


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add("car", "Tesla")
    hash_table["car"] = "Toyota"
    hash_table.add("pc", "Mac")
    hash_table.add("sns", "Youtube")
    hash_table.print()
    print(hash_table.get("car"))
    print(hash_table["sns"])
    print(hash_table.get("pc"))

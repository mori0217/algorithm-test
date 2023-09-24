from dataclasses import dataclass
from typing import Any


@dataclass
class Stack:
    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if self.items:
            return self.items.pop()
        return None


if __name__ == "__main__":
    stack = Stack()
    print(stack.items)
    stack.push(1)
    print(stack.items)
    stack.push(2)
    print(stack.items)
    stack.push(3)
    print(stack.items)
    print(stack.pop())
    print(stack.items)
    print(stack.pop())
    print(stack.items)
    print(stack.pop())
    print(stack.items)

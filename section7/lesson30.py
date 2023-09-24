from dataclasses import dataclass
from typing import Any


@dataclass
class Queue:
    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        if self.items:
            return self.items.pop(0)
        return None


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.items)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

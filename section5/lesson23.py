from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: Any
    next: Node | None = None
    prev: Node | None = None


@dataclass
class DoublyLinkedList:
    head: Node | None = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            next_node = current_node.next
            next_node.prev = None
            current_node = None
            self.head = next_node
            return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return

        next_node = current_node.next
        prev_node = current_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        current_node = None
        return

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print()
    linked_list.insert(0)
    linked_list.print()
    linked_list.remove(1)
    linked_list.print()
    linked_list.remove(3)
    linked_list.print()
    linked_list.remove(0)
    linked_list.print()
    linked_list.remove(2)
    linked_list.print()

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def insert(node: Node | None, value: int) -> Node:
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def inorder(node: Node | None) -> None:
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Node | None, value: int) -> bool:
    if node is None:
        return False
    if node.value == value:
        return True
    if value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)


def min_value(node: Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(node: Node | None, value: int) -> Node | None:
    if node is None:
        return node
    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


if __name__ == "__main__":
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    inorder(root)
    print('remove')
    root = remove(root, 6)
    inorder(root)

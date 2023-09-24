from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node | None, value: int) -> Node:
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node | None) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value: int) -> bool:
        def _search(node: Node | None, value: int) -> bool:
            if node is None:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> Node | None:
        def _remove(node: Node | None, value: int) -> Node | None:
            if node is None:
                return node
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        return _remove(self.root, value)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(6)
    tree.insert(5)
    tree.insert(7)
    tree.insert(1)
    tree.insert(10)
    tree.insert(2)
    tree.inorder()
    print(tree.search(6))
    print(tree.search(4))
    tree.remove(6)
    tree.inorder()

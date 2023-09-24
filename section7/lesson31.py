from collections import deque


def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    return new_queue


if __name__ == "__main__":
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue)
    print(reverse(queue))

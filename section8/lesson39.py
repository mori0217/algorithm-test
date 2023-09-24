from collections import Counter
import heapq


def top_n_with_heap(words: list[str], n: int) -> list[str]:
    counts = Counter(words)
    heap = [(-counts[word], word) for word in counts]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(n)]


if __name__ == "__main__":
    words = [
        "python",
        "c",
        "java",
        "go",
        "python",
        "c",
        "go",
        "go",
        "python",
        "python",
        "c",
        "c",
        "c",
        "c",
        "c",
    ]
    print(top_n_with_heap(words, 3))


def hanoi(disk: int, src: str, dest: str, support: str) -> None:
    if disk < 1:
        return

    hanoi(disk-1, src, support, dest)
    print(f"move disk {disk} from {src} to {dest}")
    hanoi(disk - 1, support, dest, src)


def get_hanoi_movement(disk: int, src: str, dest: str, support: str) -> list[tuple[int, str, str]]:
    result = []

    def _hanoi(disk: int, src: str, dest: str, support: str) -> None:
        if disk < 1:
            return
        _hanoi(disk-1, src, support, dest)
        result.append((disk, src, dest))
        _hanoi(disk-1, support, dest, src)

    _hanoi(disk, src, dest, support)
    return result


if __name__ == "__main__":
    hanoi(3, "A", "C", "B")
    for result in get_hanoi_movement(3, "A", "C", "B"):
        print(result)

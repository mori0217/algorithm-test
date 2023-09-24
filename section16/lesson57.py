import sys
import time


def fermat_last_theorem_v1(max_num: int, square_num: int) -> list[tuple[int, int, int]]:
    result = []
    if square_num < 2:
        return result

    max_z = int(((max_num - 1) ** 2 + max_num ** 2) ** (1 / square_num))
    for x in range(1, max_num + 1):
        for y in range(x+1, max_num + 1):
            for z in range(y+1, max_z):
                if x ** square_num + y ** square_num == z ** square_num:
                    result.append((x, y, z))
    return result


def fermat_last_theorem_v2(max_num: int, square_num: int) -> list[tuple[int, int, int]]:
    result = []
    if square_num < 2:
        return result

    for x in range(1, max_num + 1):
        for y in range(x+1, max_num + 1):
            pow_sum = x ** square_num + y ** square_num
            if pow_sum > sys.maxsize:
                raise ValueError('The number is too large.')

            z = int(pow_sum ** (1 / square_num))
            z_pow = z ** square_num
            if z_pow == pow_sum:
                result.append((x, y, z))
    return result


if __name__ == '__main__':

    for n in range(2, 6):
        start = time.time()
        print('v1', fermat_last_theorem_v1(20, n))
        print('v1', 'time =', time.time() - start)

        start = time.time()
        print('v2', fermat_last_theorem_v2(20, n))
        print('v2', 'time =', time.time() - start)

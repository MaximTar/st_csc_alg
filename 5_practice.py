import decimal
import sys
from functools import lru_cache

from timing import compare

sys.setrecursionlimit(5000)

cache = {}


def fib1(n):
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


def fib2(n):
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


def memo(f):
    inner_cache = {}

    def inner(n):
        if n not in inner_cache:
            cache[n] = f(n)
        return cache[n]

    return inner


@lru_cache(maxsize=None)
def fib3(n):
    return n if n <= 1 else fib3(n - 1) + fib3(n - 2)


def fib4(n):
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


# Binet formula
def fib5(n):
    root_5 = 5 ** 0.5
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


def fib6(n):
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


# https://habr.com/ru/post/148336/
def fib7(n):
    if n <= 1:
        return n

    inner_cache = {}
    q = [[1, 1], [1, 0]]
    powers = [int(pow(2, b)) for (b, d) in enumerate(reversed(bin(n - 1)[2:])) if d == '1']

    def multiply_matrices(matrix_1, matrix_2):
        """Умножение матриц (ожидаются матрицы в виде списка список размером 2x2)"""

        a11 = matrix_1[0][0] * matrix_2[0][0] + matrix_1[0][1] * matrix_2[1][0]
        a12 = matrix_1[0][0] * matrix_2[0][1] + matrix_1[0][1] * matrix_2[1][1]
        a21 = matrix_1[1][0] * matrix_2[0][0] + matrix_1[1][1] * matrix_2[1][0]
        a22 = matrix_1[1][0] * matrix_2[0][1] + matrix_1[1][1] * matrix_2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def get_matrix_power(matrix, power):
        """Возведение матрицы в степень (ожидается p равная степени двойки)"""

        if power == 1:
            return matrix
        if power in inner_cache:
            return inner_cache[power]
        matrix_power = get_matrix_power(matrix, int(power / 2))
        result_matrix = multiply_matrices(matrix_power, matrix_power)
        inner_cache[power] = result_matrix
        return result_matrix

    matrices = [get_matrix_power(q, p) for p in powers]

    while len(matrices) > 1:
        matrices.append(multiply_matrices(matrices.pop(), matrices.pop()))
    return matrices[0][0][0]


if __name__ == "__main__":
    pass
    # fib4 ~ 100
    # fib6 ~ 30_000
    # compare([fib6, fib7], list(range(0, 100_000, 100)), n_iter=100)

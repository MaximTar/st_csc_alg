import importlib
import random
import sys
from functools import lru_cache

ed = importlib.import_module('21_editing_distance')

TEST_STRING_LEN = 5
RECURSION_LIMIT = 1000

sys.setrecursionlimit(RECURSION_LIMIT)


def editing_distance_2(s1, s2):
    m, n = len(s1), len(s2)

    if n > m:
        return editing_distance_2(s2, s1)

    prev = list(range(n + 1))
    for i, ch1 in enumerate(s1, 1):
        curr = [i]
        for j, ch2 in enumerate(s2, 1):
            curr.append(min(curr[-1] + 1,
                            prev[j] + 1,
                            prev[j - 1] + (ch1 != ch2)))
        prev = curr  # .copy()
    return prev[n]


def editing_distance_1(s1, s2):
    @lru_cache(maxsize=None)
    def d(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        else:
            return min(d(i, j - 1) + 1,
                       d(i - 1, j) + 1,
                       d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]))

    return d(len(s1), len(s2))


def test(f, n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, TEST_STRING_LEN)
        s = "".join(random.choice("01") for _ in range(length))

        assert f(s, "") == f("", s) == len(s)
        assert f(s, s) == 0


if __name__ == '__main__':
    test(ed.unrecoverable_editing_distance)
    test(editing_distance_1)
    test(editing_distance_2)

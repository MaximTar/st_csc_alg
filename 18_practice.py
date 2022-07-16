from bisect import bisect_left


def find_pos(xs, query):
    lo = bisect_left(xs, query)
    # i < lo: xs[i] < query
    # i > lo: xs[i] >= query
    if lo < len(xs) and xs[lo] == query:
        return lo + 1
    else:
        return -1


def binary_search(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        idx = left + (right - left) // 2
        if lst[idx] == num:
            return idx + 1
        elif lst[idx] > num:
            right = idx - 1
        else:
            left = idx + 1
    return -1


def test():
    assert binary_search([], 42) == -1
    assert binary_search([42], 42) == 1
    assert binary_search([24], 42) == -1


if __name__ == '__main__':
    test()

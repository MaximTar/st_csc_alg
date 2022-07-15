import heapq
import sys
from random import randint

from timing import timed


def fractional_knapsack(capacity, values_and_weights):
    order = [(v / w, w) for v, w in values_and_weights]
    order.sort(reverse=True)
    accumulator = 0

    for v_per_w, w in order:
        if w < capacity:
            accumulator += v_per_w * w
            capacity -= w
        else:
            accumulator += v_per_w * capacity
            break

    return accumulator


def fractional_knapsack_2(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    accumulator = 0

    while order:
        v_per_w, w = heapq.heappop(order)
        if w < capacity:
            accumulator += -v_per_w * w
            capacity -= w
        else:
            accumulator += -v_per_w * capacity
            break

    return accumulator


def fractional_knapsack_3(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)
    accumulator = 0

    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        accumulator -= v_per_w * can_take
        capacity -= can_take

    return accumulator


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))


def test(f):
    assert f(0, [(60, 20)]) == 0.0
    assert f(25, [(60, 20)]) == 60.0
    assert f(25, [(60, 20), (0, 100)]) == 60.0
    assert f(25, [(60, 20), (50, 50)]) == 60.0 + 5.0
    assert f(50, [(60, 20), (100, 50), (120, 30)]) == 180.0

    for attempt in range(100):
        n = randint(1, 1000)
        capacity = randint(0, 2 * 10 ** 6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append((randint(0, 2 * 10 ** 6), randint(1, 2 * 10 ** 6)))

        t = timed(f, capacity, values_and_weights)
        assert t < 5


if __name__ == '__main__':
    test(fractional_knapsack)
    test(fractional_knapsack_2)
    test(fractional_knapsack_3)

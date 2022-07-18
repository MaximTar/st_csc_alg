# Вспомогательный модуль для курса "Алгоритмы: теория и практика. Методы"

import time

from matplotlib import pyplot as plt


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        acc = min(acc, time.perf_counter() - t0)

    return acc


def compare(fs, args, n_iter=100):
    xs = list(range(len(args)))
    for f in fs:
        plt.plot(xs, [timed(f, chunk, n_iter=n_iter) for chunk in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

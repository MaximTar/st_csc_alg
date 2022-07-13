def fib3(n):
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


if __name__ == "__main__":
    print(fib3(80000))

# необходимо вычислить n-е число Фибоначчи (f_0 = 0, f_1 = 1)
def fib(n):
    if n <= 1:
        return n
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 2] + lst[i - 1])
    return lst[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()

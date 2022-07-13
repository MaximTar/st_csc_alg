# необходимо найти остаток от деления n-го числа Фибоначчи на m
def fib_mod(n, m):
    if n <= 1:
        return n
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append((lst[i - 2] + lst[i - 1]) % m)
        if lst[-1] == 1 and lst[-2] == 0:
            return lst[n % (len(lst) - 2)]
        # if len(lst) > 6 * m:
        #     return n % m
    return lst[-1]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

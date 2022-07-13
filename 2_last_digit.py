# необходимо найти последнюю цифру n-го числа Фибоначчи
def fib_digit(n):
    if n <= 1:
        return n
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append((lst[i - 2] + lst[i - 1]) % 10)
    return lst[-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

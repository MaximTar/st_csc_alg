# найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых
def diff_terms(n):
    dts, nn = [], n
    for i in range(1, n + 1):
        if nn > i * 2:
            dts.append(i)
            nn -= i
        elif nn - i == 0:
            dts.append(i)
            return dts
    return dts


def main():
    n = int(input())
    dts = diff_terms(n)
    print(len(dts))
    print(*dts)


if __name__ == "__main__":
    main()

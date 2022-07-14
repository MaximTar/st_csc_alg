# найдите максимальную стоимость частей предметов,
# помещающихся в рюкзак, с точностью не менее трёх знаков после запятой


def backpack(pavs, w_max):
    if pavs:
        p, w = 0, 0
        sorted_lst = sorted(pavs, key=lambda x: x[0] / x[1], reverse=True)
        for pav in sorted_lst:
            if w + pav[1] >= w_max:
                p += (w_max - w) / pav[1] * pav[0]
                return round(p, 3)
            else:
                p += pav[0]
                w += pav[1]
        return round(p, 3)


def main():
    n, w_max = map(int, input().split())
    prices_and_volumes = []
    for _ in range(n):
        prices_and_volumes.append(list(map(int, input().split())))
    print(backpack(prices_and_volumes, w_max))


if __name__ == "__main__":
    main()

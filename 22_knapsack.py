# первая строка входа содержит целые числа 1≤W≤10**4 и 1≤n≤300 — вместимость рюкзака и число золотых слитков
# следующая строка содержит n целых чисел 0≤w_1,…,w_n≤10**5, задающих веса слитков
# найдите максимальный вес золота, который можно унести в рюкзаке


knapsack_dict = {}


def knapsack_with_repetitions(w, weights, costs, n):
    knapsack = [0] * (w + 1)
    for i in range(1, w + 1):
        for j in range(n):
            w_j = weights[j]
            if w_j <= i:
                knapsack[i] = max(knapsack[i], knapsack[i - w_j] + costs[j])
    return knapsack[-1]


def knapsack_without_repetitions_bottom_up(w, weights, costs, n):
    knapsack = [0] * (w + 1)
    knapsack = [[el] * (n + 1) for el in knapsack]
    for j in range(1, n + 1):
        for i in range(1, w + 1):
            knapsack[i][j] = knapsack[i][j - 1]
            w_j = weights[j - 1]
            if w_j <= i:
                knapsack[i][j] = max(knapsack[i][j], knapsack[i - w_j][j - 1] + costs[j - 1])
    return knapsack[-1][-1]


# TODO knapsack_withOUT_repetitions_top_down
def knapsack_with_repetitions_top_down(w, weights, costs, n):
    if w not in knapsack_dict:
        value = 0
        for j in range(n):
            w_j = weights[j]
            if w_j <= w:
                value = max(value, knapsack_with_repetitions_top_down(w - w_j, weights, costs, n) + costs[j])
        knapsack_dict[w] = value
    return knapsack_dict[w]


def main():
    w, n = map(int, input().split())
    weights = list(map(int, input().split()))
    print(knapsack_without_repetitions_bottom_up(w, weights, weights, n))


if __name__ == '__main__':
    main()

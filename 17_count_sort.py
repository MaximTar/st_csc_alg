# первая строка содержит число n, вторая — n натуральных чисел, не превышающих 10
# выведите упорядоченную по неубыванию последовательность этих чисел


def count_sort(lst, n, k=11):  # k is from 0 to 10
    helper_lst = [0] * k
    res_lst = [None] * n
    for i in range(n):
        helper_lst[lst[i]] += 1
    for i in range(1, k):
        helper_lst[i] += helper_lst[i - 1]
    for i in range(n - 1, -1, -1):
        lst_i = lst[i]
        res_lst[helper_lst[lst_i] - 1] = lst_i
        helper_lst[lst_i] -= 1
    return res_lst


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(*count_sort(nums, n))


if __name__ == '__main__':
    main()

# дано целое число n (1≤n≤10**5) и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10**9
# найдите наибольшую невозрастающую подпоследовательность в A
# в первой строке выведите её длину k, во второй — её индексы 1≤i_1<i_2<…<i_k≤n
# (таким образом, A[i_1]≥A[i_2]≥…≥A[i_n])


def reverse_bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            hi = mid
        else:
            lo = mid + 1
    return lo


# https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
def find_subsequence_indices(lst, n):
    last_elements = [10 ** 10] + [-1] * n
    predecessor_indices = [-1] * n
    smallest_value_indices = [-1] * (n + 1)

    length = 0
    for i in range(n):
        lst_i = lst[i]
        idx = reverse_bisect_left(last_elements, lst_i, hi=length + 1)
        last_elements[idx] = lst_i
        predecessor_indices[i] = smallest_value_indices[idx - 1]
        smallest_value_indices[idx] = i
        if idx >= length:
            length = idx

    return_indices = [-1] * length
    k = smallest_value_indices[length]
    for i in range(length - 1, -1, -1):
        return_indices[i] = k + 1
        k = predecessor_indices[k]
    return length, return_indices


# N ** 2
# def find_subsequence_indices(lst, n):
#     lengths = [1] * n
#     for i in range(n):
#         for j in range(i):
#             if lst[i] <= lst[j] and lengths[j] + 1 > lengths[i]:
#                 lengths[i] = lengths[j] + 1
#
#     max_value = max(lengths)
#     max_value_return = max_value
#
#     # subsequence = [0] * max_value
#     # for i in range(n - 1, -1, -1):
#     #     if lengths[i] == max_value:
#     #         subsequence[max_value - 1] = lst[i]
#     #         max_value -= 1
#     # return subsequence
#
#     indices = [0] * max_value
#     for i in range(n - 1, -1, -1):
#         if lengths[i] == max_value:
#             indices[max_value - 1] = i + 1
#             max_value -= 1
#     return max_value_return, indices


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    length, subsequence_indices = find_subsequence_indices(lst, n)
    print(length)
    print(*subsequence_indices)


if __name__ == '__main__':
    main()

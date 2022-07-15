# первая строка содержит число n, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 10^9
# необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i] > A[j]
# такая пара элементов называется инверсией массива
# количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
# например, в упорядоченном по неубыванию массиве инверсий нет вообще,
# а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента
from collections import deque


def merge(lst_1, lst_2):
    len_lst_1, len_lst_2 = len(lst_1), len(lst_2)
    # res_lst, counter = [], 0
    res_lst, counter = [None] * (len_lst_1 + len_lst_2), 0
    res_idx, idx_1, idx_2 = 0, 0, 0
    a, b = None, None
    while lst_1 or lst_2 or a or b:
        if a is None:
            try:
                # a = lst_1.pop(0)
                a = lst_1[idx_1]
                idx_1 += 1
            except IndexError:
                if b:
                    # res_lst.append(b)
                    res_lst[res_idx] = b
                    res_idx += 1
                # res_lst += lst_2[idx_2:]
                res_lst = res_lst[:res_idx] + lst_2[idx_2:]
                return res_lst, counter
        if b is None:
            try:
                # b = lst_2.pop(0)
                b = lst_2[idx_2]
                idx_2 += 1
            except IndexError:
                if a:
                    # res_lst.append(a)
                    res_lst[res_idx] = a
                    res_idx += 1
                # res_lst += lst_1[idx_1:]
                res_lst = res_lst[:res_idx] + lst_1[idx_1:]
                return res_lst, counter
        if a <= b:
            # res_lst.append(a)
            res_lst[res_idx] = a
            res_idx += 1
            a = None
        else:
            # res_lst.append(b)
            res_lst[res_idx] = b
            res_idx += 1
            counter += len_lst_1 - idx_1 + 1
            b = None
    return res_lst, counter


def iterative_merge_sort(lst):
    # sorted_lst, counter = [], 0
    sorted_lst, counter = deque(), 0
    for el in lst:
        sorted_lst.append([el])
    while len(sorted_lst) > 1:
        # lst, c = merge(sorted_lst.pop(0), sorted_lst.pop(0))
        lst, c = merge(sorted_lst.popleft(), sorted_lst.popleft())
        sorted_lst.append(lst)
        counter += c

    # return sorted_lst.pop(0), counter
    return sorted_lst.popleft(), counter


def shift_bit_length(x):
    return 1 << (x - 1).bit_length()


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    k = 10 ** 10
    # while len(lst) < shift_bit_length(len(lst)):
    #     lst.append(k)
    lst += [k] * (shift_bit_length(n) - n)
    _, c = iterative_merge_sort(lst)
    # print(_)
    print(c)


if __name__ == '__main__':
    main()

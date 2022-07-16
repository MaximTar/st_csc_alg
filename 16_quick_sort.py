# в первой строке задано два целых числа n и m — количество отрезков и точек на прямой, соответственно
# следующие n строк содержат по два целых числа a_i и b_i — координаты концов отрезков
# последняя строка содержит m целых чисел — координаты точек
# все координаты не превышают 10^8 по модулю
# точка считается принадлежащей отрезку, если она находится внутри него или на границе
# для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит
from random import randint


def binary_count_less(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        idx = left + (right - left) // 2
        lst_idx = lst[idx]
        if lst_idx == num:
            right = idx - 1
        elif lst_idx > num:
            right = idx - 1
        else:
            left = idx + 1
    return left + (right - left) // 2


def binary_count_less_or_equal(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        idx = left + (right - left) // 2
        lst_idx = lst[idx]
        if lst_idx == num:
            left = idx + 1
        elif lst_idx > num:
            right = idx - 1
        else:
            left = idx + 1
    return left + (right - left) // 2


# def partition(lst, left, right):
#     pivot, less_idx = lst[left], left
#     for i in range(left + 1, right):
#         if lst[i] <= pivot:
#             less_idx += 1
#             lst[i], lst[less_idx] = lst[less_idx], lst[i]
#     lst[left], lst[less_idx] = lst[less_idx], lst[left]
#     return less_idx
#
#
# def quick_sort_simple(lst, left, right):
#     while left < right:
#         m = partition(lst, left, right)
#         # элиминация хвостовой рекурсии для более длинного списка
#         if m - left > right - m + 1:
#             quick_sort_simple(lst, left, m)
#             left = m + 1
#         else:
#             quick_sort_simple(lst, m + 1, right)
#             right = m


# https://gist.github.com/adonese/4bf34d5b57ee0358626c
def partition_3(lst, left, right):
    pivot, idx, less, greater = lst[left], left, left, right
    while idx <= greater:
        lst_idx = lst[idx]
        if lst_idx < pivot:
            lst[less], lst[idx] = lst_idx, lst[less]
            less += 1
            idx += 1
        elif lst_idx > pivot:
            lst[idx], lst[greater] = lst[greater], lst_idx
            greater -= 1
        else:
            idx += 1

    return less, greater


def quick_sort_3_random(lst, left, right):
    while left < right:
        k = randint(left, right)
        lst[k], lst[left] = lst[left], lst[k]

        less, greater = partition_3(lst, left, right)

        if less - 1 - left > right - greater + 1:
            quick_sort_3_random(lst, left, less - 1)
            left = greater + 1
        else:
            quick_sort_3_random(lst, greater + 1, right)
            right = less - 1


def main():
    n, _ = map(int, input().split())
    start_segments, end_segments = [], []
    for _ in range(n):
        s, e = map(int, input().split())
        start_segments.append(s)
        end_segments.append(e)
    points = map(int, input().split())
    quick_sort_3_random(start_segments, 0, n - 1)
    quick_sort_3_random(end_segments, 0, n - 1)
    for pt in points:
        print(binary_count_less_or_equal(start_segments, pt) - binary_count_less(end_segments, pt), end=" ")


if __name__ == '__main__':
    main()

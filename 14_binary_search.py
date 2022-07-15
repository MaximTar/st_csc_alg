# в первой строке даны целое число n и массив А из n различных натуральных чисел в порядке возрастания,
# во второй — целое число k и k натуральных чисел b_1 ... b_k
# для каждого i от 1 до k необходимо вывести индекс j, для которого A[j] = b_i или −1, если такого j нет.


def binary_search(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        idx = left + (right - left) // 2
        if lst[idx] == num:
            return idx + 1
        elif lst[idx] > num:
            right = idx - 1
        else:
            left = idx + 1
    return -1


def main():
    _, *lst = map(int, input().split())
    _, *nums = map(int, input().split())
    print(*[binary_search(lst, n) for n in nums], sep=" ")


if __name__ == '__main__':
    main()

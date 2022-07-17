# дано целое число n и массив A[1…n] натуральных чисел
# выведите максимальное k, для которого найдётся подпоследовательность длины k,
# в которой каждый элемент делится на предыдущий


def find_subsequence_lengths(lst, n):
    lengths = [1] * n
    for i in range(n):
        for j in range(i):
            if lst[i] % lst[j] == 0 and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
    return lengths


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    subsequence_lengths = find_subsequence_lengths(lst, n)
    print(max(subsequence_lengths))


if __name__ == '__main__':
    main()

# у вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
# заменить xx на 2x, 3x или x+1
# по данному целому числу 1≤n≤10**5 определите минимальное число операций k, необходимое, чтобы получить n из 1
# выведите k и последовательность промежуточных чисел


nums_dict = {1: 0}


def reverse_calculate_dict(n):
    # wrong
    # if n in nums_dict:
    #     return nums_dict[n]
    # if n % 3 == 0:
    #     nums_dict[n] = reverse_calculate(n / 3) + 1
    #     return nums_dict[n]
    # if n % 2 == 0:
    #     nums_dict[n] = reverse_calculate(n / 2) + 1
    #     return nums_dict[n]
    # nums_dict[n] = reverse_calculate(n - 1) + 1

    # spike?
    n = int(n)
    if n in nums_dict:
        return nums_dict[n]
    if n % 3 == 0:
        nums_dict[n] = reverse_calculate_dict(n / 3) + 1
        return nums_dict[n]
    nums_dict[n] = int(min(reverse_calculate_dict(n / 2) + 1 if n % 2 == 0 else 10 ** 5,
                           reverse_calculate_dict(n - 1) + 1))

    # bad solution?
    # if n in nums_dict:
    #     return nums_dict[n]
    # nums_dict[n] = min(reverse_calculate(n - 1) + 1,  # because of this
    #                    reverse_calculate(n / 2) + 1 if n % 2 == 0 else 10 ** 5,
    #                    reverse_calculate(n / 3) + 1 if n % 3 == 0 else 10 ** 5)

    return nums_dict[n]


def main():
    n = int(input())
    print(reverse_calculate_dict(n))

    # yes, we could just collect pointer on previous element in dict {key: (min_steps, pointer)}, but...
    # sequence recovery
    sequence, counter, last_n = [n] * (nums_dict[n] + 1), nums_dict[n] - 1, n
    for key in reversed(nums_dict.keys()):  # not good
        if nums_dict[key] == counter and (last_n / 3 == key or last_n / 2 == key or last_n - 1 == key):
            sequence[counter], counter, last_n = key, counter - 1, key
    print(*sequence)


if __name__ == '__main__':
    main()

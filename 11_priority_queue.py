# первая строка входа содержит число операций
# каждая из последующих n строк задают операцию одного из следующих двух типов:
# Insert x / ExtractMax
# первая операция добавляет число x в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его
import sys


def insert(lst, el):
    lst.append(el)
    # sift up
    idx = len(lst) - 1
    while idx != 0 and lst[idx] > lst[(idx - 1) // 2]:
        lst[idx], lst[(idx - 1) // 2] = lst[(idx - 1) // 2], lst[idx]
        idx = (idx - 1) // 2


def extract_max(lst):
    try:
        print(lst[0])
    except IndexError:
        return
    # sift down
    try:
        lst[0] = lst.pop(-1)  # if len(lst) > 1
    except IndexError:
        return
    idx = 0
    while True:
        if len(lst) > 2 * idx + 2:
            child_left, child_right = lst[2 * idx + 1], lst[2 * idx + 2]
            if child_left > child_right:
                if lst[idx] < child_left:
                    lst[idx], lst[2 * idx + 1] = lst[2 * idx + 1], lst[idx]
                    idx = 2 * idx + 1
                elif lst[idx] < child_right:
                    lst[idx], lst[2 * idx + 2] = lst[2 * idx + 2], lst[idx]
                    idx = 2 * idx + 2
                else:
                    return
            else:
                if lst[idx] < child_right:
                    lst[idx], lst[2 * idx + 2] = lst[2 * idx + 2], lst[idx]
                    idx = 2 * idx + 2
                elif lst[idx] < child_left:
                    lst[idx], lst[2 * idx + 1] = lst[2 * idx + 1], lst[idx]
                    idx = 2 * idx + 1
                else:
                    return
        elif len(lst) > 2 * idx + 1:
            child_left = lst[2 * idx + 1]
            if lst[idx] < child_left:
                lst[idx], lst[2 * idx + 1] = lst[2 * idx + 1], lst[idx]
                idx = 2 * idx + 1
            else:
                return
        else:
            return


def operate(operations):
    max_heap = []
    for operation in operations:
        if operation.startswith("Insert"):
            insert(max_heap, int(operation.split()[1]))
        elif operation.startswith("ExtractMax"):
            extract_max(max_heap)


def main():
    n = int(sys.stdin.readline())
    operations = []
    for _ in range(n):
        operations.append(sys.stdin.readline())
    operate(operations)


if __name__ == "__main__":
    main()

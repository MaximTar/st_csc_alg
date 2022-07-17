# вычислите расстояние редактирования двух данных непустых строк длины не более 10**2
# содержащих строчные буквы латинского алфавита


# def insertion_cost(symbol):
#     return 1
# def deletion_cost(symbol):
#     return 1
INSERTION_COST = 1
DELETION_COST = 1


def substitution_cost(first_symbol, second_symbol):
    return 0 if first_symbol == second_symbol else 1


def recoverable_editing_distance_matrix(first_string, second_string):
    n, m = len(first_string) + 1, len(second_string) + 1
    distance_matrix = [0] * n
    distance_matrix = [[el] * m for el in distance_matrix]

    for i in range(n):
        distance_matrix[i][0] = i
    for i in range(m):
        distance_matrix[0][i] = i
    for i in range(1, n):
        for j in range(1, m):
            distance_matrix[i][j] = min(distance_matrix[i - 1][j] + INSERTION_COST,
                                        distance_matrix[i][j - 1] + DELETION_COST,
                                        distance_matrix[i - 1][j - 1] + substitution_cost(first_string[i - 1],
                                                                                          second_string[j - 1]))

    return distance_matrix


def unrecoverable_editing_distance(first_string, second_string):
    n, m = len(first_string) + 1, len(second_string) + 1

    if n > m:
        previous_line, current_line = [0] * m, [0] * m
        first_string, second_string, n, m = second_string, first_string, m, n
    else:
        previous_line, current_line = [0] * n, [0] * n

    for i in range(n):
        previous_line[i] = i
    for j in range(1, m):
        current_line[0] = j
        for i in range(1, n):
            current_line[i] = min(current_line[i - 1] + INSERTION_COST,
                                  previous_line[i] + DELETION_COST,
                                  previous_line[i - 1] + substitution_cost(first_string[i - 1],
                                                                           second_string[j - 1]))
        previous_line = current_line.copy()

    return current_line[-1]


def main():
    first_string = input()
    second_string = input()
    # print(recoverable_editing_distance_matrix(first_string, second_string)[-1][-1])
    print(unrecoverable_editing_distance(first_string, second_string))


if __name__ == '__main__':
    main()

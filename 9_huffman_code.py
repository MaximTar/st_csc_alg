# постройте оптимальный беспрефиксный код
# в первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки
# в следующих k строках запишите коды букв в формате "letter: code"
# в последней строке выведите закодированную строку.


def huffman_code(inp):
    letters = {}
    for letter in inp:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    priorities = sorted(list(letters.items()), key=lambda x: x[1])
    priorities_new = []  # priorities.copy()

    if len(priorities) == 1:
        for key in letters:
            letters[key] = "0"
        new_string = ""
        for letter in inp:
            new_string += letters[letter]
        return letters, new_string

    while len(priorities) > 1:
        l, r = priorities.pop(0), priorities.pop(0)
        priorities_new.append((l[0], 0))
        priorities_new.append((r[0], 1))
        priorities.append((l[0] + r[0], l[1] + r[1]))
        priorities = sorted(priorities, key=lambda x: x[1])
    priorities_new = sorted(priorities_new, key=lambda x: len(x[0]), reverse=True)

    for key in letters:
        new_val = ""
        for priority in priorities_new:
            if key in priority[0]:
                new_val += str(priority[1])
        letters[key] = new_val

    new_string = ""
    for letter in inp:
        new_string += letters[letter]

    return letters, new_string


def main():
    inp = str(input())
    letters, new_string = huffman_code(inp)
    keys = letters.keys()
    print(len(keys), len(new_string))
    for key in keys:
        print("{}: {}".format(key, letters[key]))
    print(new_string)


if __name__ == "__main__":
    main()

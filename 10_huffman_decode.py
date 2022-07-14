# восстановите строку по её коду и беспрефиксному коду символов
# в первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
# встречающихся в строке, и размер получившейся закодированной строки, соответственно
# в следующих k строках записаны коды букв в формате "letter: code"
# ни один код не является префиксом другого
# буквы могут быть перечислены в любом порядке
# в качестве букв могут встречаться лишь строчные буквы латинского алфавита
# каждая из этих букв встречается в строке хотя бы один раз
# наконец, в последней строке записана закодированная строка
# исходная строка и коды всех букв непусты
# заданный код таков, что закодированная строка имеет минимальный возможный размер


def huffman_decode(letters, coded_string):
    decoded_str = ""

    letter = ""
    for symbol in coded_string:
        letter += symbol
        for key in letters.keys():
            if letters[key] == letter:
                decoded_str += key
                letter = ""

    return decoded_str


def main():
    k, _ = map(int, input().split())
    letters = {}
    for _ in range(k):
        letter, frequency = map(str, input().split(": "))
        letters[letter] = frequency
    coded_string = str(input())

    print(huffman_decode(letters, coded_string))


if __name__ == "__main__":
    main()

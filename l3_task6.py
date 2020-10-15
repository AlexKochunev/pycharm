def extract_str1(s):
    """
    Функция форматирования слова,если слово состоит из элементов строки low_s то вернётся это слово с большой буквы,
    в противном случае вернётся пустая строка
    :param s: строка
    :return: строка
    """
    low_s = 'abcdefghijklmnopqrstuvwxyz'
    for c in s:
        if low_s.find(c) == -1:
            return ''
    return s[0:1].upper()+s[1:]


def extract_str(s):
    """
    Функция форматирования слова,если слово состаит из маленьких латинских букв то вернётся это слово с большой буквы,
    в противном случае вернётся пустая строка
    :param s: строка
    :return: строка
    """
    for c in s:
        if c < 'a' or c > 'z':
            return ''
    return s[0:1].upper()+s[1:]


in_list = input("Введите строку:").split()
for i, j in enumerate(in_list):
    in_list[i] = extract_str(j)
print(f'Выходная строка: {" ".join(in_list)}')

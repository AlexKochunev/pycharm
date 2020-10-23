with open("test.txt", "w", encoding="UTF-8") as my_file:
    while my_file.write(input('Введите строку для добавления(выход - пустая строка):') + '\n') != len('\n'):
        pass

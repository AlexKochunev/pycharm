with open("test.txt", "r", encoding="UTF-8") as my_file:
    content = my_file.readlines()
    print(f'Всего строк - {len(content)}')
    for i, line in enumerate(content):
        words = line.split()
        print(f'В {i+1} строке содержится {len(words)} слов.')

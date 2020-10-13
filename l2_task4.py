my_str = input("Введите строку из нескольких слов разделённых пробелом:")
my_list = my_str.split()
for i, n in enumerate(my_list):
    print(f'{i+1} слово - {n[:10]}')

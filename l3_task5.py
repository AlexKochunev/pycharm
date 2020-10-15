# не знаю где здесь процедуру использовать
numbers_arr = []
g_exit = False
while True:
    in_list = input("Введите последовательность чисел, разделённых пробелом (для выхода введите 'Q')").split()
    t = 0
    for i in in_list:
        if i == "Q":
            g_exit = True
            break
        try:
            numbers_arr.append(float(i))
            t += float(i)
        except ValueError:
            print(f"Невозможно представить {i} как число")
    print(f'Сумма послежовательности {numbers_arr} = {sum(numbers_arr)} ({t}) ')
    if g_exit:
        break

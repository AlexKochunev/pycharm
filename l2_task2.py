item = ''
my_list = []
while item != "Q":
    item = input('Добавте значения в список, для завершения введите "Q": ')
    if item == "Q":
        break
    my_list.append(item)
    print(f'Исходный список - {my_list}')
print(f'Исходный список -   {my_list}')
for i in range(len(my_list) // 2):
    t = my_list[2 * i]
    my_list[2 * i] = my_list[(2 * i) + 1]
    my_list[(2 * i) + 1] = t
print(f'Изменённый список - {my_list}')

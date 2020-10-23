import random


s = 1
my_list = []
while s != 0:
    my_list.append(str(s))
    s = random.randint(0, 100)
with open("test.txt", "w", encoding="UTF-8") as my_file:
    my_file.write(' '.join(my_list))
with open("test.txt", "r", encoding="UTF-8") as my_file:
    my_list = my_file.readline().split()
    s = 0
    for i in my_list:
        s += int(i)
print(f'Сумма всех чисел - {s}')

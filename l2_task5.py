my_list = [7, 5, 3, 3, 2]
item = ''
while True:
    item = input('Добавте значения в рейтинг, для завершения введите не число: ')
    if item.isdigit():
        score = int(item)
        for i, n in enumerate(my_list):
            if score > n:
                my_list.insert(i, score)
                score = None
                break
        if score is not None:
            my_list.append(score)
        print(f'Текущий рейтинг - {my_list}')
    else:
        break

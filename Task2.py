seconds = int(input('Введите количество секунд:'))
print(f'Вы указали {seconds // 3600:02}:{(seconds % 3600) // 60 :02}:{seconds % 60:02}')

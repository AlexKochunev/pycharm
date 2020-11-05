class MyListError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        inp_str = input("Добавить число в список ('stop' для выхода):")
        if inp_str.upper() == "STOP":
            break
        if inp_str.isdigit():
            my_list.append(inp_str)
        else:
            raise MyListError(f'{inp_str} Не число!')
    except MyListError as err:
        print(err)
print(','.join(my_list))

my_dict = dict()
with open("text_6.txt", "r", encoding="UTF-8") as my_file:
    context = my_file.readlines()
    for s in context:
        my_list = s.split(':')
        my_dict[my_list[0]] = sum([
            int(hours.strip()) for hours in
            my_list[1].replace(')', '(').replace('-', '(').split('(') if hours.strip().isdigit()])
print(f'{my_dict}')

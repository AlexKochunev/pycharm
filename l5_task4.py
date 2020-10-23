with open("text_4.txt", "r", encoding="UTF-8") as my_in_file, open("test_out.txt", "w", encoding="UTF-8") as my_out_file:
    content = my_in_file.readlines()
    for i, line in enumerate(content):
        words = line.split(" - ")
        if len(words) == 2:
            if words[0].upper() == 'ONE':
                my_out_file.write('Один - '+words[1])
            elif words[0].upper() == 'TWO':
                my_out_file.write('Два - '+words[1])
            elif words[0].upper() == 'THREE':
                my_out_file.write('Три - '+words[1])
            elif words[0].upper() == 'FOUR':
                my_out_file.write('Четыре - '+words[1])
        else:
            my_out_file.write(line)

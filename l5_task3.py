with open("text_3.txt", "r", encoding="UTF-8") as my_file:
    content = my_file.readlines()
    employees = 0
    avg_salary = 0
    for i, line in enumerate(content):
        try:
            words = line.split()
            if len(words) == 2:
                surname = words[0]
                salary = float(words[1])
                employees += 1
                avg_salary += salary
                if salary < 20000:
                    print(f'Сотрудник {surname} получает менее 20000 а именно - {salary}')
        except ValueError:
            continue
if employees > 0:
    print(f'Средняя зарплата - {avg_salary/employees}')
else:
    print('Сотрудники 404')

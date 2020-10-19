from sys import argv


def calc_salary(work_h, payment_h, prize):
    try:
        return float(work_h)*float(payment_h)+float(prize)
    except ValueError:
        return "Запуск программы возможен только с числовыми параметрами"


if len(argv) != 4:
    print("Запуск программы возможен с параметрами: \n"
          "1-й параметр(число) - время работы сотрудника в часах\n"
          "2-й параметр(число) - оплата труда в час\n"
          "3-й параметр(число) - премия сотрудника")
else:
    print(f"Зарплата сотрудника равна {calc_salary(argv[1],argv[2],argv[3])}")

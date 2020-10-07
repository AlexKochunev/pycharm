income = int(input('Прибыль:'))
outcome = int(input('Издержки:'))

if income > outcome:
    #    print(f'Ура, работаем в плюс. Прибыль составила - {income-outcome} , '
    #          f'рентабельность - {((income-outcome)/income)*100:.2f}%')
    print(f'Ура, работаем в плюс. Прибыль составила - {income - outcome} , '
          f'рентабельность - {((income - outcome) / income):.2%}')
    workers = int(input('Укажите количество сотрудников вашей организации:'))
    print(f'Прибыль на 1 сотрудника составляет -  {((income - outcome) / workers):.0f}')
else:
    print(f'Работаем в минус :( . Убытки составляют - {outcome - income}')

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


emp = Position('Александр', 'Кочунёв', 'Программист', 1000, 5000)
print(f'Полное имя сотрудника - {emp.get_full_name()}')
print(f'Общий доход сотрудника - {emp.get_total_income()}')

class MyIndexError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    name = ''
    page_size = ''

    def __init__(self, name, page_size='A4'):
        self.name = name
        self.page_size = page_size


class Printer(OfficeEquipment):
    toner_type = ''

    def __str__(self):
        return self.name + ' page size - ' + self.page_size + ' toner type - ' + self.toner_type


class Scanner(OfficeEquipment):
    dpi = 160

    def __str__(self):
        return self.name + ' page size - ' + self.page_size + ' dpi - ' + str(self.dpi)


class Copier(OfficeEquipment):
    page_per_minute = 100

    def __str__(self):
        return self.name + ' page size - ' + self.page_size + ' speed - ' + str(self.page_per_minute) + ' page per minute'


class Stocks:
    printers = []
    scanners = []
    copiers = []

    def add_printer(self, printer):
        self.printers.append(printer)

    def add_scanner(self, scanner):
        self.scanners.append(scanner)

    def add_copiers(self, copier):
        self.copiers.append(copier)

    def take_printer(self, index):
        if index in range(len(self.printers)):
            self.printers.pop(index)
        else:
            raise MyIndexError(f'Принтер {index} не найден, укажите id из списка принтеров')

    def take_scanner(self, index):
        if index in range(len(self.scanners)):
            self.scanners.pop(index)
        else:
            raise MyIndexError(f'Сканер {index} не найден, укажите id из списка сканеров')

    def take_copier(self, index):
        if index in range(len(self.copiers)):
            self.copiers.pop(index)
        else:
            raise MyIndexError(f'Ксерокс {index} не найден, укажите id из списка ксерексов')

    def print_printers(self):
        return '\n'.join(str(i) + ' - ' + str(s) for i, s in enumerate(self.printers))

    def print_scanners(self):
        return '\n'.join(str(i) + ' - ' + str(s) for i, s in enumerate(self.scanners))

    def print_copiers(self):
        return '\n'.join(str(i) + ' - ' + str(s) for i, s in enumerate(self.copiers))


print('Добро пожаловать на склад оргтехники.\nВыберите действие ')
stock = Stocks()
stock.add_printer(Printer('Test'))
stock.add_printer(Printer('Test1', 'A2'))
stock.add_printer(Printer('Test2', 'A3'))
stock.add_printer(Printer('Test3', 'A0'))
stock.add_scanner(Scanner('Test'))
stock.add_scanner(Scanner('Test1', 'A2'))
stock.add_scanner(Scanner('Test2', 'A3'))
stock.add_scanner(Scanner('Test3', 'A0'))
stock.add_copiers(Copier('Test'))
stock.add_copiers(Copier('Test1', 'A2'))
stock.add_copiers(Copier('Test2', 'A3'))
stock.add_copiers(Copier('Test3', 'A0'))
while True:
    action = input('1-Просмотр 2-Добавление 3-Списание Q-Выход:')
    if action == '1':
        action = input('1-Принтеры 2-Сканеры 3-Копиры:')
        if action == '1':
            print(stock.print_printers())
        elif action == '2':
            print(stock.print_scanners())
        elif action == '3':
            print(stock.print_copiers())
    elif action == '2':
        action = input('1-Принтеры 2-Сканеры 3-Копиры:')
        if action == '1':
            stock.add_printer(Printer(input('Введите имя и формат принтера через пробел:')))
        elif action == '2':
            stock.add_scanner(Scanner(input('Введите имя и формат сканера через пробел:')))
        elif action == '3':
            stock.add_copiers(Copier(input('Введите имя и формат ксерокса через пробел:')))
    elif action == '3':
        action = input('1-Принтеры 2-Сканеры 3-Копиры:')
        try:
            if action == '1':
                stock.take_printer(int(input('Введите id принтера:')))
            elif action == '2':
                stock.take_scanner(int(input('Введите id сканера:')))
            elif action == '3':
                stock.take_copiers(int(input('Введите id ксерокса:')))
        except ValueError:
            print("Параметра не число")
        except MyIndexError as err:
            print(err)
    elif action == 'Q':
        break

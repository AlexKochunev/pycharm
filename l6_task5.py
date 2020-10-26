class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашем')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


my_stationery = Stationery()
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()

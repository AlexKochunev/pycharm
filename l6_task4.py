class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    _direction = ''

    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self, speed='39'):
        if speed.isdigit():
            self.speed = int(speed)
        print(f'Машина поехала со скоростью {self.speed} км/ч')

    def show_speed(self):
        print(f'Машина двигается со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def tern(self, direction='Прямо'):
        self._direction = direction
        print(f'Текущее направление движения - {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение!!!, скорость {self.speed} км/ч, максимально разрешённая - 60 км/ч')
        else:
            print(f'Машина двигается со скоростью {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение!!!, скорость {self.speed} км/ч, максимально разрешённая - 40 км/ч')
        else:
            print(f'Машина двигается со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)


c = Car(20, None, 'Undefined', None)
tc = TownCar(58, 'White', 'Nissan')
wc = WorkCar(35, 'Green', 'Lada')
sc = SportCar(229, 'Red', 'lamborghini')
pc = PoliceCar(163, 'Blue', 'Chevrolet')
c.show_speed()
tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()
c.tern('Лево')
tc.tern('Право')
wc.tern('Верх')
sc.tern('Низ')
pc.tern()
c.stop()
tc.stop()
wc.stop()
sc.stop()
pc.stop()
c.go('99')
tc.go('79')
wc.go('65')
sc.go('115')
pc.go('2')
c.show_speed()
tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()
c.stop()
tc.stop()
wc.stop()
sc.stop()
pc.stop()
c.speed = 100
tc.speed = 88
wc.speed = 84
sc.speed = 65
pc.speed = 11
c.show_speed()
tc.show_speed()
wc.show_speed()
sc.show_speed()
pc.show_speed()

from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name=''):
        self.name = name

    @property
    @abstractmethod
    def s(self):
        pass

    @s.setter
    @abstractmethod
    def s(self, s):
        pass


class Coat(Cloth):
    def __init__(self, v=50):
        Cloth.__init__(self, 'Пальто')
        self.v = v

    @property
    def s(self):
        return self.v/6.5 + 0.5

    @s.setter
    def s(self, s):
        self.v = int((s-0.5)*6.5)


class Suit(Cloth):
    def __init__(self, h=185):
        Cloth.__init__(self, 'Костюм')
        self.h = h

    @property
    def s(self):
        return 2 * self.h + 0.3

    @s.setter
    def s(self, s):
        self.h = int((s-0.3)/2)


C = Coat(52)
S = Suit(180)
print(f'{C.name} {S.name} {C.s+S.s}')
C.s = 10
print(f'{C.v}')
S.s = 300
print(f'{S.h}')

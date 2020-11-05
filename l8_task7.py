class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum((self.a * other.a) - (self.b * other.b), (self.b * other.a) + (self.a * other.b))

    def __str__(self):
        if self.b < 0:
            return f'{self.a}{self.b}i'
        else:
            return f'{self.a}+{self.b}i'


c1 = ComplexNum(2, 3)
c2 = ComplexNum(5, -7)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)

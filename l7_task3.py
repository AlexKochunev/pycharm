class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __floordiv__(self, other):
        return Cell(self.cell//other.cell)

    def __str__(self):
        return f'Всего {self.cell} клеток'

    def __add__(self, other):
        return Cell(self.cell+other.cell)

    def __sub__(self, other):
        return Cell(self.cell-other.cell) if self.cell > other.cell else 'Error'

    def __mul__(self, other):
        return Cell(self.cell*other.cell)

    def make_order(self, in_line):
        return ('*\t'*in_line+'\n')*(self.cell//in_line)+('*\t'*(self.cell % in_line)+'\n')


C1 = Cell(10)
print(C1.make_order(3))
C2 = Cell(5)
print(C2.make_order(10))
print(C1+C2)
print(C1-C2)
print(C1*C2)
print(C1//C2)

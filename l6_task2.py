class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        return self._width*self._length*0.125


rd = Road(5000, 20)
print(f'Масса дорожного покрытия = {rd.calc_weight()}')

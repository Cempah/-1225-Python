class Road:

    def __init__(self, _length, _width, _weight, _thickness):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._thickness = _thickness

    def mass(self):
        mass_all = self._length * self._width * self._weight * self._thickness
        return (f"{self._length}м * {self._width}м * {self._weight}кг * {self._thickness}см = {mass_all}кг")


r = Road(20, 5000, 25, 5)
print(r.mass())
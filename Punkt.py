import math


class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)  # zwracam odleglosc


class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __sub__(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2)


if __name__ == '__main__':
    print(Punkt2D(2, 2) - Punkt2D(0, 0))
    print(Punkt3D(2, 2, 1) - Punkt3D(0, 0, 0))

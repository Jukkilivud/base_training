import math


class Point:
    pass


p1 = Point()
p2 = Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p1.y)
print(p2.x, p2.y, '\n')


class Point:
    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
print(p.x, p.y, '\n')


class Point:
    def reset():
        pass


try:
    p = Point()
    p.reset()
except NameError:
    print("Нет такой переменной!")
except TypeError:
    print("Лошара, забыл self добавить, надо Point(self)!", '\n')


# Передача нескольких аргументов.
class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


point1 = Point()
point2 = Point()
point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1), '\n')


# Инициализация объекта.

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


point = Point(3, 5)
print(point.x, point.y)

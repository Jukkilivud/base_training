import random
from pathlib import Path
import abc
import logging
from functools import wraps
from typing import Type, Any, cast

a = random.choice((1, 2, 3))
b = random.randint(1, 535)
print(a, '\n', b, '\n')

home = Path.home()
print(home)

#  Этот код определяет несколько классов и методов, которые помогают моделировать игру с кубиками.
# Код начинается с импорта необходимых модулей: random, pathlib, и abc (Abstract Base Classes). Затем выполняется несколько простых операций с использованием модуля random и pathlib.
# Определяется абстрактный базовый класс Die, который представляет общий интерфейс для всех кубиков. Класс имеет абстрактный метод __init__, который должен быть реализован в производных классах, и атрибут face, который хранит текущее значение кубика.
# Затем определяется класс DDice, который представляет собой набор кубиков. Конструктор класса принимает произвольное количество аргументов, каждый из которых представляет собой класс, наследующийся от Die. Эти классы используются для создания экземпляров кубиков и хранения их в атрибуте dice. Класс также имеет атрибут adjust, который представляет собой начальное смещение для общего значения кубиков.
# Класс DDice имеет следующие методы:
# plus: устанавливает начальное смещение для общего значения кубиков и возвращает экземпляр DDice.
# roll: бросает все кубики в наборе.
# total: вычисляет общее значение кубиков, добавляя начальное смещение.
# __add__: позволяет добавить к экземпляру DDice новый кубик или начальное смещение.
# __radd__: позволяет добавить к новому кубику экземпляр DDice или начальное смещение.
# __mul__: позволяет умножить экземпляр DDice на целое число, создавая новый экземпляр DDice с повторенными кубиками.
# __rmul__: позволяет умножить целое число на экземпляр DDice, создавая новый экземпляр DDice с повторенными кубиками.
# Этот код предоставляет основу для моделирования игры с кубиками и может быть расширен для реализации более сложных правил игры.


class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.face}"


class DDice:
    def __init__(self, *die_class: Type[Die]) -> None:
        self.dice = [dc() for dc in die_class]
        self.adjust: int = 0

    def plus(self, adjust: int = 0) -> 'DDice':
        self.adjust = adjust
        return self

    def roll(self) -> None:
        for d in self.dice:
            d.roll()

    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust

    def __add__(self, die_class: Any) -> 'DDice':
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [type(d) for d in self.dice] + [die_class]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __radd__(self, die_class: Any) -> 'DDice':
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [die_class] + [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented

    def __mul__(self, n: Any) -> 'DDice':
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented

    def __rmul__(self, n: Any) -> 'DDice':
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented


class DieMeta(abc.ABCMeta):
    def __new__(metaclass: Type[type], name: str, bases: tuple[type, ...], namespace: dict[str, Any], **kwargs: Any,) -> "DieMeta":
        if 'roll' in namespace and not getattr(namespace['roll'], "__isabstractmethod__", False):
            namespace.setdefault('logger', logging.gerLogger(name))
            original_method = namespace['roll']

            @wraps(original_method)
            def logged_roll(self: 'DieLog') -> None:
                original_method(self)
                self.logger.info(f"Rolled {self.face}")
            namespace['roll'] = logged_roll
        new_object = cast('DieMeta', abc.ABCMeta.__new__(
            metaclass, name, bases, namespace))
        return new_object


class DieLog(metaclass=DieMeta):
    logger: logging.Logger

    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.face}"

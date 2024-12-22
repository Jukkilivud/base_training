from typing import List, Union


class EvenOnly(List[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Добавлять можно только целые числа")
        if value % 2 != 0:
            raise ValueError("Добавлять можно только чётные числа")
        super().append(value)


e = EvenOnly()
# e.append("a string")
# e.append(3)

# Вложенные блоки exception


def funniest_division(divider: int) -> Union[str, float]:
    try:
        if divider == 13:
            raise ValueError("13 несчастливое число")
        return 100 / divider
    except ZeroDivisionError:
        return "Введите число отличное от нуля"
    except TypeError:
        return "Введите число"
    except ValueError:
        print("Нет, нет, только не 13!!")
        raise


s = funniest_division(divider=0)
print(s)


# finally
some_exception = [ValueError, TypeError, IndexError, None]
for choice in some_exception:
    try:
        print(f"\nRaising {choice}")
        if choice:
            raise choice("An error")
        else:
            print("no exception raised")
    except ValueError:
        print("Перехвачено a ValueError")
    except TypeError:
        print("Перехвачено a TypeError")
    except Exception as ex:
        print(f"Перехвачена другая ошибка: {e.__class__.__name__}")
    else:
        print("Этот код вызывается, если исключение отсутствует")
    finally:
        print("Этот код вызывается всегда")


# Создание шаблонов CSV
class InvalidSampleError:
    """Файл исходных данных имеет недопустимое представление данных"""


@classmethod
def from_dict(cls, row: dict[str, str]) -> "KnownSample":  # type:ignore
    if row['species'] not in {"Iris-setosa", "Iris-versecolour", "Iris-virginica"}:
        raise InvalidSampleError(f"invalid species in {row!r}")
    try:
        return cls(
            species=row['species'],
            sepal_lenght=float(row["sepal_lenght"]),
            sepal_width=float(row["sepal_width"]),
            petal_lenght=float(row["petal_lenght"]),
            petal_width=float(row["petal_width"]),
        )
    except ValueError as exc:
        raise InvalidSampleError(f"invalid {row!r}")

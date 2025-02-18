"""Сгенерировать забавные имена, случайно комбинируя имена из двух отдельных списков."""

import sys
import random


def main():
    """Случайно выбрать имена из двух кортежей имён и вывести на экран."""

    print("\nДобро пожаловать в приложение 'Подбор имён.'\n")
    print("Прикольное имя:")
    first = ('Дятел', 'Долбаёб', 'Олень')
    midle = ('Чушпан', 'Дегенерат', 'Шизик')
    last = ('Хуесосович', 'Членович', 'Пиздолизович')
    while True:
        first_name = random.choice(first)
        midle_name = random.choice(midle)
        last_name = random.choice(last)
        print("\n")
        print(f"{first_name} {midle_name} {last_name}", file=sys.stderr)
        # print("\n")
        try_again = input(
            "\nПопробуете ещё? (Нажмите Enter Либо n, чтобы выйти)\n")
        if try_again.lower() == 'n':
            break
    input("\nНажмите Enter для завершения работы.")


if __name__ == 'main':
    main()
main()

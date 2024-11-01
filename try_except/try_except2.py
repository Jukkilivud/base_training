import logging


# Создание пользовательского исключения
print("Program started")
try:
    raise Exception("User Exception!")
except Exception as e:
    print(str(e))
print("Program finished", '\n')


# class NegativeAge(Exception):
#     pass


# print("Program started")
# try:
#     age = int(input("Введите ваш возраст: "))
#     if age < 18 or age > 99:
#         raise NegativeAge("Exception: Пшол вон отсюда!!!")
#     print('Добро пожаловать!')
# except NegativeAge as e:
#     print(e)
# print("Program finished", '\n')


# Запись исключений в лог.
logging.basicConfig(filename="log.txt", level=logging.INFO)
try:
    print(10 / 0)
except Exception as x:
    logging.error(str(x))

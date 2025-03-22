# from datetime import date
# import pytz
import datetime


def email(pochta: str) -> bool:
    mail = ['gmail.com', 'mail.ru', 'ya.ru']
    if pochta.endswith(tuple(mail)):
        return True
    else:
        return False


m = email('sadf@gmail.com')
print(m)
m1 = email('sadf@gail.com')
print(m1)
m2 = email('sadf@ya.ru')
print(m2)


def merge(lst: list) -> list:
    merge_list = []
    for i in lst:
        for o in str(i):
            merge_list.append(int(o))
    return merge_list


sp = merge([123, 456, 789])
print(sp)


def user_tel(number: int) -> str:
    # try:
    if len(str(number)) == 11 and str(number)[0] == '8':
        return f"Номер {number} принят"
    if len(str(number)) != 11:
        return "Введите корректный, 11-ти значный, номер телефона"
    if str(number)[0] != '8':
        return "Набор номера через 8"
    # except Exception:
    #     return "Ваш номер не будет зарегистрирован!"


telephone = user_tel(89130331212)
print(telephone)
telephone1 = user_tel(32922331212)
print(telephone1)
telephone2 = user_tel(8882922331212)
print(telephone2)

print('\n')


def medium_num(*args: int) -> int:
    medium_total = []
    medium_total.append(args)
    print(medium_total)
    sum_medium = sum(args) / len(args)
    return f"Средне арифметическое введённых чисел равно: {int(sum_medium)}"


num_user = medium_num(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(num_user)
num_user01 = medium_num(10, 10, 100, 40)
print(num_user01)


def sum_digit(num: int) -> str:
    list_01 = str(num)
    if len(list_01) == 6:
        return f"Сумма пар чисел {num} равна: {int(list_01[:2]) + int(list_01[2:4]) + int(list_01[4:6])}"
    if len(list_01) < 5:
        return f"Что-то пошло не так..."


digits = sum_digit(123456)
print(digits)
digits1 = sum_digit(3456)
print(digits1)

str_01 = "Дана строка со словами. Отсортируйте слова в алфавитном порядке."
str_sorted = str_01.lower()
str_sorted = str_sorted.split()
print(sorted(str_sorted))

str_02 = '2025-2-1'
pleas_split = str_02.split('-')
str_03 = []
for i in pleas_split:
    if len(i) == 4:
        str_03.append(i)
    if len(i) < 2:
        str_03.append(i.zfill(2))
print('-'.join(str_03))

str_04 = ''
for num in range(1, 6):
    str_04 += str(num) + '-'
print('-', str_04, sep='')

text = "Дана строка с текстом. Получите процентное содержание каждого символа текста в виде словаря, в котором ключами будут символы, а значениями - их процентное содержание."
dict_alfavit = {}
total_chars = len(text)

for char in text:
    if char in dict_alfavit:
        dict_alfavit[char] += 1
    else:
        dict_alfavit[char] = 1

for char in dict_alfavit:
    dict_alfavit[char] = (dict_alfavit[char] / total_chars) * 100

print(dict_alfavit)

str_05 = '1234567'
str_05 = str(str_05[::-1])
ls = ''
for i in range(len(str_05)):
    ls += str_05[i]
    if (i + 1) % 3 == 0 and i != len(str_05) - 1:
        ls += ' '
print(ls[::-1])


def randommm(rang, rang2):
    import random
    random_numbers = [random.randint(rang, rang2) for _ in range(10)]
    return random_numbers


x = randommm(1, 100)
print(x)

data = [i for i in range(0, 10)]
print(data)
data2 = [i for i in 'Love']
print(data2)
data3 = [i for i in range(10) if i % 2 == 0]
print(data3)
data4 = [i * j for i in range(3) for j in range(3)]
print(data4)
data5 = [[i*j for i in range(3)] for j in range(3)]
print(data5)
data6 = [[0 for x in range(3)] for y in range(3)]
print(data6)
data7 = [(lambda i: i*i)(i) for i in range(10)]
print(data7)


def repitt(i1: int, i2: int) -> list:
    import itertools
    data8 = [i for i in itertools.repeat(i1, i2)]
    return data8


x_data = repitt(1, 5)
print(x_data)

str_06 = '12345678'
str_07 = ''
for i in range(len(str_06)):
    str_07 += str_06[i]
    if (i + 1) % 2 == 0 and i != len(str_06) - 1:
        str_07 += ' '
print(str_07)

list_01 = [1, 2, 3, 3, 4, 5]
for i in range(len(list_01) - 1):
    if list_01[i] == list_01[i + 1]:
        print('Есть повторяющиеся цифры.')
        break
else:
    print('Нет повторяющихся цифр.')

print(f"\n\n\n       Чутка попрактикуем с datetime:")


def date1():
    import datetime
    from datetime import date
    d = datetime.datetime.now()
    d1 = date.today()
    d2 = d.time()
    return f"{d} \n{d1} \n{d2}"


date01 = date1()
print(date01)

time_object = datetime.time(12, 45, 56)
print(time_object)
time_object2 = datetime.date(2015, 12, 26)
print(time_object2)
time_object3 = datetime.timedelta(20)
print(time_object3)

f_date = datetime.date(2024, 11, 3)
s_date = datetime.date(2025, 11, 3)
delta = s_date - f_date
print(delta)
past_date = datetime.datetime.today() + datetime.timedelta(days=365)
print(past_date)

now = datetime.time(9, 31, 0)
next_hour = datetime.time(10, 31, 0)
print('now < next_hour:', now < next_hour)
today = datetime.date.today()
next_week = datetime.date.today() + datetime.timedelta(days=7)
print('today > next_week:', today > next_week)

dt_now = datetime.datetime.now(datetime.UTC)
print(dt_now)

print('\n')


def today_1():
    day = datetime.date.today()  # Получение сегодняшней даты
    day1 = day.strftime('%A')  # Получение названия дня недели
    return day1


d = today_1()
print(d)


def today_now(date: int) -> str:
    # Вывод из введённой даты названия месяца и дня недели
    return date.strftime('%B  %A')


d1 = datetime.date(2025, 1, 21)  # Ввести нужную дату
day_of_week = today_now(d1)
print(day_of_week)

# Сделайте функцию, которая параметром будет принимать секунды, а возвращать количество суток, соответствующих этим секундам.


def total_days(sec: int) -> float:
    """Возвращает колличество дней из секунд, с округлением до сотых."""
    return round(sec / (24*60*60), 2)


d2 = total_days(86500)
print(f"Количество дней = {d2}")

print('\n')


def trim_number(num: int, text: str) -> str:
    """функция, которая параметром принимает число и строку, и обрезает эту строку до длины, заданной первым параметром."""
    new_text = ''
    text_s = text.split()
    for i in range(num):
        if i < len(text_s):
            new_text += text_s[i] + ' '
    return new_text.strip()


txt = trim_number(
    5, 'Возвращает колличество дней из секунд, с округлением до сотых')
print(txt)


def sum_division(num: int) -> int:
    """Сделайте функцию, которая параметром будет принимать число, а возвращать сумму его делителей."""
    lst_01 = []
    for i in range(1, int(num)+1):
        if int(num) % i == 0:
            lst_01.append(i)
    return sum(lst_01), lst_01


num1 = sum_division(6)
print(num1)
num2 = sum_division(10)
print(num2)
# num3 = sum_division('a')
# print(num3)


def not_zero(num: int) -> int:
    """Сделайте функцию, которая параметром будет принимать число и удалять из него нули."""
    # return str(num).rstrip('0')
    zero_not = []
    for i in str(num):
        if i != '0':
            zero_not.append(i)
    return int(''.join(zero_not))


num01 = not_zero(6010)
print(num01)
# num02 = not_zero(0.6023410000000)
# print(num02)

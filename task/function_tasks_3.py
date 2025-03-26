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


def double_list(lst: list) -> list:
    """Сделайте функцию, которая параметром будет принимать список и удалять из него все дубли."""
    new_list = []
    return list(set(lst))


lst_1 = double_list([1, 2, 2, 33, 4, 4])
print(lst_1)


def three_double_list(lst: list) -> list:
    '''Сделайте функцию, которая параметром будет принимать список и удалять из него все дубли, которые встречаются больше трех раз.'''
    from collections import Counter
    counter = Counter(lst)
    new_list = [item for item, count in counter.items() if count <= 3]
    return new_list


lst_2 = three_double_list([1, 2, 2, 4, 4, 2, 2, 1, 1, 1, 33, 33])
print(lst_2)


def double_nearby(lst: list) -> list:
    """Сделайте функцию, которая параметром будет принимать список и удалять из него одинаковые, рядом стоящие элементы."""
    new_list = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_list.append(lst[i])
    return new_list


lst_3 = double_nearby([1, 2, 2, 4, 4, 3, 2, 1, 1, 1, 33, 33])
print(lst_3)


def max_min_dict(lst: list) -> dict:
    """Сделайте функцию, которая параметром будет принимать список с числами и возвращать максимальное и минимальное значение из этого списка в виде следующего словаря:{'max': 9,'min': 1,}"""
    dct = {'max': max(lst),
           'min': min(lst)}
    return dct


lst_02 = max_min_dict([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(lst_02)


def division_count(num: int) -> str:
    """Сделайте функцию, которая параметром будет принимать число, а возвращать количество его делителей."""
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return f"Колличество делителей для числа {num} = {count}"


num_1 = division_count(64)
print(num_1)
num_2 = division_count(4)
print(num_2)


def division_count_list(num: int) -> str:
    """Сделайте функцию, которая параметром будет принимать число, а возвращать список его делителей."""
    count = []
    for i in range(1, num+1):
        if num % i == 0:
            count.append(i)
    return f"Список делителей числа {num} = {count}"


num_11 = division_count_list(4)
print(num_11)
num_12 = division_count_list(64)
print(num_12)


def prime_number(num: int) -> bool:
    """Сделайте функцию, которая параметром будет принимать число и проверять, простое оно или нет."""
    if num < 2:
        return None
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num02 = prime_number(3)
print(num02)
num03 = prime_number(6)
print(num03)
num04 = prime_number(1)
print(num04)


def even_num(num: int) -> int:
    """Сделайте функцию, которая параметром будет принимать число и удалять из него четные цифры."""
    even = []
    for i in str(num):
        if int(i) % 2 != 0:
            even.append(i)
    return int(''.join(even))


num05 = even_num(123456)
print(num05)


def random_num(num1: int, num2: int, num3: int) -> list:
    """Сделайте функцию, которая заполнит список N случайными числами из заданного промежутка."""
    import random
    N = [random.randint(num1, num2) for _ in range(num3)]
    return N


num06 = random_num(1, 15, 5)
print(f"Случайные числа из заданного диапазона {num06}")


def what_num(arg: str) -> bool:
    """Дана переменная со строкой. Проверьте, что в эта строка представляет собой число, то есть состоит только из цифр."""
    if str(arg).isdigit():
        return True
    return False


arg = what_num('123')
print(arg)
arg1 = what_num('asdf10')
print(arg1)


def what_decimal(arg: str) -> bool:
    """Дана переменная со строкой. Проверьте, что эта строка представляет собой дробь."""
    try:
        float_value = float(arg)
        return float_value != int(float_value)
    except ValueError:
        return False


arg2 = what_decimal('2.12')
print(arg2)
arg3 = what_decimal('212')
print(arg3)
arg4 = what_decimal('sdf')
print(arg4)


def list_num(text: list) -> int:
    """Сделайте функцию, которая параметром будет принимать список с числами и возвращать второе по величине число."""
    sort_list = sorted(text)
    return f"Второе по виличине число из списка {text} = {sort_list[1]}"


text1 = list_num([1, 7, 4, 3])
print(text1)
text2 = list_num([122, 567, 323])
print(text2)


def list_num_sort(num1: int, num2: int) -> list:
    """Сделайте функцию, которая параметрами будет принимать два числа и возвращать список, заполненный целыми числами от минимального параметра до максимального."""
    list_sort = []
    for i in range(min(num1, num2), max(num1, num2)+1):
        list_sort.append(i)
    return sorted(list_sort)


num07 = list_num_sort(1, 5)
print(num07)
num08 = list_num_sort(10, 1)
print(num08)


def alphabet(num_letters: int = 26) -> list:
    """Сделайте функцию, которая заполнит список случайными латинскими буквами."""
    import string
    import random
    abc_list = list(string.ascii_lowercase)
    return random.sample(abc_list, min(num_letters, 26))


abc = alphabet(5)
print(abc)


def fibonachi_n(fib: int) -> int:
    """    Возвращает сумму первых N чисел Фибоначчи.
    Keyword arguments:
    argument -- Количество чисел Фибоначчи для суммирования
    Return: Сумма первых N чисел Фибоначчи
    """
    if fib <= 0:
        return 0
    elif fib == 1:
        return 0
    elif fib == 2:
        return 1

    fib_sum = 0
    a, b = 0, 1
    for _ in range(fib):
        print(f"Число Фибоначчи: {_}")
        fib_sum += a
        a, b = b, a+b
    return fib_sum


fib = fibonachi_n(5)
print(fib)

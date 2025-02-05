# 1.1
def negative_num(num):
    if num >= 0:
        return ('Positive')
    else:
        return ('Negative')


x = negative_num(10)
y = negative_num(-10)
print(x, y)

# 1.2


def random_string(string):
    print(f"Длинна строки {len(string)} символа.")


random_string('Здесь будет 23 символов')
random_string('0000')


# 1.3
def random_string_2(string):
    print(string[-1])


random_string_2('asd')
random_string_2('12345')

# 1.4


def random_number(num):
    if num % 2 == 0:
        print(f"Число {num} чётное.")
    else:
        print(f"Число {num} не чётно.")


random_number(10)
random_number(33)

# 1.5


def two_word(word1, word2):
    if word1[:1] == word2[:1]:
        print("Первые буквы этих слов совпадают!")
    else:
        print("Первые буквы этих слов не совпадают!")


two_word('sex', 'sony')
two_word('asd', 'sdf')

# 1.6


def soft_sign(word):
    if word[-1:] == 'ь':
        print(word[-2:-1])
    else:
        print(word[-1:])


soft_sign('глухомань')
soft_sign('что')

# 2.1, 2.2, 2.3, 2.4, 2.5


def one_num(num1):
    print(str(num1)[:1])
    print(str(num1)[-1:])
    a = str(num1)[:1]
    b = str(num1)[-1:]
    summ = int(a) + int(b)
    print(f"{a} + {b} = {summ}")
    print(len(str(num1)))


one_num(102)
one_num(5123)

# 2.2


def x(num1, num2):
    if str(num1)[:1] == str(num2)[:1]:
        print('True')
    else:
        print('False')


x(12, 15)
x(12, 54)
x('gdf', 'ghe')

# 1.2.6

a = [1, 2, 3, 4, 5, 6]


def slice(lst1):
    print(lst1[:3])


slice(a)

# 1.3.1


def str_singl(string) -> str:
    if len(string) > 1:
        print(string[-2:-1])


str_singl('assdgfsdgd')

# 1.3.2


def division_num(num1, num2) -> str:
    if num1 % num2 == 0:
        print('True')
    else:
        print('False')


division_num(10, 5)
division_num(10, 3)

# 1.3.3


def getting_characters(string) -> list:
    print(list(string))


getting_characters('abcdfg')

# 1.3.4
lst = [1, 2, 3, 4, 5, 6]
print(lst[2:5])

# 1.3.5


def data_format(data: dict) -> str:
    x = dict.values(data)
    print('-'.join(x), '\n')


data_format({'y': '2025', 'm': '12', 'd': '31'})

# 1.3.6


def integers(num1, num2):
    for z in range(num1, num2 + 1):
        print(z, end=' ')


integers(1, 100)
integers(-100, 0)

for z in range(100, 0, -1):
    print(z, end=' ')


def even_nums(num1: int, num2: int):
    print('\n', 'Чётные числа: ')
    for num in range(num1, num2):
        if num % 2 == 0:
            print(num, end=' ')
    print('\n', 'Кратные трём: ')
    for t in range(num1, num2):
        if t % 3 == 0:
            print(t, end=' ')


even_nums(1, 100)
# even_nums(9, 100)

lst1 = [1, 2, 3, 4, 5, 6]
print('\n', lst1[-2:])

s = 'abcdeabc'
print(list(s[:5]))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i, end=' ')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b)
print(list(c))


a = 'asd'
b = 'dsa'
if a == b[::-1]:
    print('palindrom')


def problem(a):
    if isinstance(a, str):
        return 'Error'
    elif isinstance(a, int):
        return (a*50+6)


f = problem(5)
print(f)


def sum_num(*num1: int):
    sumnum = 0
    for i in range(*num1):
        sumnum += i
    return sumnum


d = sum_num(1, 100)
print(f"Сумма всех целых чисел = {d}")


def strds(n: int, n2: int):
    sumnum = 0
    for i in range(n, n2):
        if i % 2 == 0:
            sumnum += i
    return sumnum


s = strds(1, 100)
print(f"Чётные числа, сумма = {s}")


def strds(*n: int):
    sumnum = 0
    for i in range(*n):
        if i % 2 != 0:
            sumnum += i
    return sumnum


s = strds(1, 100)
print(f"Сумма всех нечётных чисел = {s}")


def remains_division(n: int, n1: int) -> int:
    return n % n1


j = remains_division(10, 3)
print(f"Остаток от деления = {j}")

lst2 = [1, 2, 3, 4, 5, 6]
print(lst2[::2])
print(sum(lst2))

sum_root = 0
for i in lst2:
    sum_root += i*2
print(sum_root)


def list_positive(lis: list):
    s = 0
    for num in lis:
        if num >= 0:
            s += num
    return s


d = list_positive([1, 2, -3, -5, 4])
print(d)


def ss(lst):
    list_one = 0
    for num in lst:
        if 0 < num < 10:
            list_one += num
    return list_one


s = ss([-1, 2, -3, 4, 5, 11])
print(s)


str1 = 'abcde'
for i in str1[::-1]:
    print(i, end='')

print(list(str1))

dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
sum_dict = sum(dct.values())
print(sum_dict)
dct2 = {'Ключ-'+k: v*2 for k, v in dct.items()}
print(f"Какждое значение словаря {dct} увеличено в 2 раза: {dct2}")
print("Значения словаря {dct} = ", list(dct.values()))


sum_dict2 = 0
for i in dct.values():
    sum_dict2 += i ** 2
print(sum_dict2)

num = 12345
print(list(str(num)))
print(list(str(num))[::-1])
print(str(num)[::-1])

num1 = list(str(num))
sum_num1 = sum(int(digit) for digit in num1)
print(sum_num1)

tpl = (1, 2, 3, 4, 5)
sm = sum(tpl)
print(sm)

list_num = [1, 2, 3, 4, 5]
num_10 = 0
for i in list_num:
    num_10 += (int(i) + (int(i)/100*10))
    num_1 = (int(i) + (int(i)/100*10))
    print(f"Число {i} увеличенно на 10%: {num_1}")
print(f"Сумма чисел, увеличенных на 10% = {num_10}")

str2 = 'abcdef'
print(str2[:3])
print(str2[::2])


def http(string: list):
    str3 = []
    str3 = [string for string in string if string.startswith('http://')]
    # for i in string:
    #     if str(i) == 'http://':
    #         str3.append(i)
    return str3


x = http(['122', 'http://', 'sdf', 'etfg'])
print(x)


def zero_position(string: str):
    zero = list(string).index('0')
    return f"Функция, позиция первого нуля = {zero}"


zp = zero_position(('123403000'))
print(zp)

sd = '23030'
dd = list(sd).index('0')
print(f"Позиция первого нуля в строке {sd} = {dd}")


def variable(list_var: list, valuee: any) -> list:
    new_list = [item for item in list_var if item != valuee]
    return new_list


jj = variable([1, 2, 3, 4, 4], 4)
print(jj)

for var in range(10, 1000):
    if int(str(var)[0]) + int(str(var)[1]) == 5:
        print(var, end=', ')

str3 = 'abcdeabc'
ddd = set(str3)
print(''.join(ddd))


def negative_number(lst: list) -> int:
    negative = []
    for num in lst:
        if num < 0:
            negative.append(num)
    return len(negative)


a = negative_number([-16, 1, -5, -1, -2])
print(f"Отрицательных чисел в этом списке: {a} числа(-ел). ")

lst3 = [-123, 1, 2, -3, -4, 76]
positive_list = []
for i in lst3:
    if i >= 0:
        positive_list.append(i)
        print(positive_list)

string = 'asdf'
new_list = list(string)
new_list.pop((-2))
print(''.join(new_list))

str4 = ['sdf.html', 'sdfs.ru', 'sde.html']
ff = [i for i in str4 if i.endswith('.html')]
print(ff)

list_float = [1.456, 2.125, 3.32, 4.1, 5.34]
intr = [round(i, 1) for i in list_float]
print(intr)


def one_second(word1: str, word2: str) -> str:
    if word1[-1:] == word2[:1]:
        return True
    else:
        return False


x = one_second('som', 'moon')
cc = one_second('sdf', 'sdfe')
print(x, cc)


def find_third_zero(string):
    count = 0
    for i, char in enumerate(string):
        if char == '0':
            count += 1
            if count == 3:
                return i
    return -1, ('В строке меньше трёх нулей!')


print(find_third_zero(string='0100'), end=' ')
w = find_third_zero('010103')
w1 = find_third_zero('4050')
print(w, w1)

numbers = '12, 34, 56'
numbers = numbers.split(',')
count = 0
for i in numbers:
    if len(i) >= 1:
        count += int(i)
print((count))


def сумма_двух_чисел(arg1: int, arg2: int) -> int:
    return arg1 + arg2


print(сумма_двух_чисел(10, 10000))

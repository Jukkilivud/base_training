# 1.1
def negative_num(num):
    if num >= 0:
        print('Positive')
    else:
        print('Negative')


negative_num(10)
negative_num(-10)


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
    print('-'.join(x))


data_format({'y': '2025', 'm': '12', 'd': '31'})

# 1.3.6


def integers(num1, num2):
    for z in range(num1, num2 + 1):
        print(z, end=' ')


integers(1, 100)
integers(-100, 0)
integers(100, 1)

# for z in range(100, 1, -1):
#     print(z, end=' ')

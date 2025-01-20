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

num_1 = -10
if num_1 < 0:
    print('число отрицательное', '\n')

str_1 = 'asdf'
print(len(str_1), '\n')

str_1
print(str_1[-1:], '\n')

num_2 = 11
if num_2 % 2 == 0:
    print('число чётное')
else:
    print('числон не чётное')

word_1 = 'asdf'
word_2 = 'affe'
if word_1[:1] == word_2[:1]:
    print('первые буквы совпадают совпадают')
else:
    print('No!!!')

# Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.
word_3 = 'приветь'
if word_3[-1:] == 'ь':
    print(word_3[-2:-1])
else:
    print(word_3[-1:])

# Дано число. Выведите в консоль первую цифру этого числа.
num_3 = 125
s = str(num_3)
print(s[:1])
print(s[-1:])
print(len(s))
# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
d = int(s[:1])
c = int(s[-1:])
print(d+c)

# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
num_4 = 179
s2 = (str(num_4))
if s[:1] == s2[:1]:
    print('Yes')
else:
    print('No')


list_1 = [1, 2, 3, 4, 5, 6]
print(list_1[:3], '\n')

# Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.
str_2 = 'asdf'
if len(str_2) > 1:
    print(str_2[-2:-1])
else:
    print("One symbol")

num_5 = 10
num_6 = 5
if num_5 % num_6 == 0:
    print("Делится без остатка")
else:
    print("No!")

string = 'abcde'
print(list(string))

list_2 = [1, 2, 3, 4, 5, 6]
a = list_2[2:5]
print(a)

dict_1 = {'year': '2025', 'month': '12', 'day': '31', }
b = '-'.join(dict_1.values())
print(b)

# Выведите в консоль все целые числа от 1 до 100.
# for c in range(1, 101):
#     print(c)

# for c in range(-100, 1):
#     print(c)

# for c in range(100, 0, -1):
#     print(c)

# for c in range(1, 100):
#     if c % 2 == 0:
#         print(c)

# for c in range(1, 100):
#     if c % 3 == 0:
#         print(c)

list_3 = [1, 2, 3, 4, 5, 6]
print(list_3[-2:])

string_1 = 'abcdeabc'
s = set(string_1)
print(s)

# Найдите сумму всех целых чисел от 1 до 100.
sumary = 0
for i in range(1, 101):
    sumary += i
print(sumary)

# Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
sumary = 0
for i in range(1, 101):
    if i % 2 == 0:
        sumary += i
print(sumary)

# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
sumary = 0
for i in range(1, 11):
    if i % 2 != 0:
        sumary += i
print(sumary)

i = 12
i2 = 5
print(i % i2)

list_4 = [1, 2, 3, 4, 5, 6]
print(list_4[::2])

# Найдите сумму элементов этого списка.
summ = sum(list_4)
print(summ)

# Найдите сумму квадратов элементов этого списка.
summ = sum(list_4 * 2)
print(summ)

# Найдите сумму квадратных корней элементов этого списка.
summ = sum(i ** 0.5 for i in list_4)
print(summ)

list_5 = [1, 2, -3, 4, -5]
sum_2 = 0
for d in list_5:
    if d > 0:
        sum_2 += d
print(sum_2)

list_6 = [-1, 2, -3, 4, 5, 11]
sum_3 = 0
for i in list_6:
    if 10 < i > 0:
        sum_3 += i
print(sum_3)

# Переберите и выведите в консоль по очереди все символы с конца строки.
str_3 = 'abcde'
for i in str_3[::-1]:
    print(i)

# Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a) & set(b)
print(list(c), '\n')

# Напишите программу для слияния нескольких словарей в один.
d_a = {1: 10, 2: 20}
d_b = {3: 30, 4: 40}
d_c = {5: 50, 6: 60}
d_u = {}
for i in (d_a, d_b, d_c):
    d_u.update(i)
print(d_u)

# Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
max_key = sorted(my_dict, key=my_dict.get)
top_3_key = max_key[-3:]
print(top_3_key, '\n')

# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
s = 'шалаш'
if s == s[::-1]:
    print(True)
else:
    print(False)

# Найдите сумму элементов этого словаря.
dct = {
    1: {1: 11, 2: 12, 3: 13, },
    2: {1: 21, 2: 22, 3: 23, },
    3: {1: 24, 2: 25, 3: 26, },
}
sum_values = 0
for i in dct:
    for j in dct[i]:
        sum_values += dct[i][j]
print(sum_values, '\n')

# Дан список. Удалите из него каждый пятый элемент.
lst = [1, 1, 1, 1, 3, 4, 1, 1, 1, 2, 5]
for i in range(4, len(lst), 5):
    lst.pop(i)
print(lst)

# Даны два числа. Получите список общих делителей этих чисел.
num1 = 12
num2 = 6
num_div = []
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        num_div.append(i)
print(num_div)

# Получите кортеж цифр, которые есть и в одном, и в другом числе:
txt1 = 12345
txt2 = 45678
tpl = set(str(txt1)) & set(str(txt2))
print(tuple(tpl), '\n')

# Найдите сумму элементов этого списка.
lst1 = [
    [
        [11, 12, 13],
        [14, 15, 16],
        [17, 17, 19],
    ],
    [
        [21, 22, 23],
        [24, 25, 26],
        [27, 27, 29],
    ],
    [
        [31, 32, 33],
        [34, 35, 36],
        [37, 37, 39],
    ],
]
fs = [num for sublist1 in lst1 for sublist2 in sublist1 for num in sublist2]
ss = sum(fs)
print(ss, '\n')

# Дан список с числами. Оставьте в нем только те числа, которые делятся на 5.
list12 = [1, 5, 15, 8]
filtered_list = [i for i in list12 if i % 5 == 0]
print(filtered_list, '\n')

# Дано число. Проверьте, что у этого числа есть только один делитель, кроме него самого и единицы.
n = 6
if int(n ** 0.5) ** 2 == n:
    result = True
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            result = False
            break
else:
    result = False
print(result)

# Найдите сумму элементов этого словаря.


def sum_dict_values(dct_1):
    sum_values = 0
    for values in dct.values():
        if sum(values):
            sum_values += sum(values)
    return sum_values


print(sum_values)


dct_1 = {
    1: {
        1: 11,
        2: 12,
        3: 13,
    },
    2: {
        1: 21,
        2: 22,
        3: 23,
    },
    3: {
        1: 24,
        2: 25,
        3: 26,
    },
}

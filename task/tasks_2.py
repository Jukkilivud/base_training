dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
sum_1 = sum(dct.values())
print(sum_1)
sum_2 = sum(dct.values()) ** 2
print(sum_2)

str_1 = 'abcde'
print(list(str_1))

num_1 = 12345
lst = str(num_1)
print(list(lst))
print(list(lst[::-1]))

# Найдите сумму цифр этого числа.
num_2 = 12345
sum_3 = 0
for i in list(str(num_2)):
    sum_3 += int(i)
print(sum_3)

tpl_1 = (1, 2, 3, 4, 5)
print(sum(tpl_1))

lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [i * 1.1 for i in lst_1]
print(lst_2, '\n')

str_2 = 'abcdef'
print(str_2[:3])
print(str_2[3:])
print(str_2[::2])  # Каждый второй символ

# Увеличьте каждое число из словаря в 2 раза:
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
dct_2 = {key: value * 2 for key, value in dct.items()}
print(dct_2)

# Выведите в консоль все его символы с конца.
num_3 = list(str(num_1))
reversed_num = int(''.join(num_3[::-1]))
print(reversed_num)

# Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://. (Два варианта решения)
lst_3 = ['asd', 'http://', 'http://', 'fee', 'http://']
for i in lst_3:
    # if i == 'http://':
    if i.startswith('http://'):
        print(i)

# Дана некоторая строка. Найдите позицию первого нуля в строке.
str_3 = '3000123'
print(str_3.find('0'))

# Дан список. Удалите из него элементы с заданным значением.
lst_3.remove('fee')
print(lst_3, '\n')

# Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.
for s in range(10, 1001):
    str_s = str(s)
    if int(str_s[0])+int(str_s[1]) == 5:
        print(s)

# Очистите строку от дублей символов
str_4 = 'abcdeabc'
double_s = ''.join(set(str_4))
print(double_s)

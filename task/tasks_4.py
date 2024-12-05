# Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.
string = '5ds3kd'
position = -1
for index, char in enumerate(string):
    if char.isdigit():
        position = index
        break
print(f"Позиция первой цифры в строке {string}: {position}", '\n')

# Дано число. Выведите в консоль количество четных цифр в этом числе.
num_1 = 123456
count = 0
for digit in str(num_1):
    if int(digit) % 2 == 0:
        count += 1
print(f"Количество чётных цифр в числе {num_1}: {count} цифры", '\n')

# Получите список его ключей:
dict_1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
keys = dict_1.keys()
print(list(keys), '\n')

# Переведите в верхний регистр все нечетные буквы этой строки. В нашем случае должно получится следующее:
string_2 = 'abcde'
result = ''
for index, char in enumerate(string_2):
    if index % 2 == 0:
        result += char.upper()
    else:
        result += char
print(f"Нечётные буквы в строке {string_2} стали заглавные: {result}", '\n')

# Сделайте заглавным первый символ каждого слова в этой строке. В нашем случае должно получится следующее:
string_3 = 'aaa bbb ccc'
ss = string_3.title()
print(f"Первая буква каждого слова стала заглавной: {ss}", '\n')

# Преобразуйте эту дату в следующий кортеж:
date = '2025-12-31'
tpl = date.split('-')
tpl = tuple(tpl[::-1])
print(tpl, '\n')

# Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.
str_1 = 'a3f5f10'
positions = [i for i, char in enumerate(str_1) if char.isdigit()]
print(positions, '\n')

# Смените регистр букв этой строки на противоположный. В нашем случае должно получится следующее:
str_2 = 'AbCdE'
up_reg = str_2.swapcase()
print(up_reg, '\n')

# Слейте пары элементов вместе:
lst_1 = [1, 2, 3, 4, 5, 6]
result = [str(i) + str(j) for i, j in zip(lst_1[::2], lst_1[1::2])]
int_list = [int(i) for i in result]
print(int_list)

# Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее:
str_3 = 'aaa bbb ccc eee fff'
up_reg_2 = [word.capitalize() if index % 2 != 0 else word for index,
            word in enumerate(str_3.split())]
result = ' '.join(up_reg_2)
print(result, '\n')

# Дан символ. Узнайте, в каком регистре этот символ - в верхнем или нижнем.
symbol = 'к'
for i in symbol:
    if i in symbol.upper():
        print(f"Символ {symbol} в верхнем регистре.")
    else:
        print(f"Символ {symbol} в нижнем регистре.")

# Удалите из этого числа все нечетные цифры. В нашем случае получится такой результат: 28
num_2 = '123789'
even_num = ''
for i in num_2:
    if int(i) % 2 == 0:
        even_num += i
print(f"Вот чётные цифры: {even_num}, из этого числа: {num_2}", '\n')

# Преобразуйте эту дату в следующий словарь:
date_tuple = ('2025', '12', '31')
year, month, day = date.split('-')
dict_date = {
    'year': year,
    'month': month,
    'day': day
}
print(dict_date)

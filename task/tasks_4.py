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
print(tuple(tpl))

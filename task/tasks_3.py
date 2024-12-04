# Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
count = 0
lst = [1, -1, 5, -3, -39]
for i in lst:
    if i < 0:
        count += 1
print(count, '\n')

# Дан список с числами. Оставьте в нем только положительные числа.
count_positive = 0
for i in lst:
    if i > 0:
        count_positive += i
        print(count_positive)

# Дана строка. Удалите предпоследний символ из этой строки.
str_1 = 'asdfghjl'
str_1 = str_1[:-2] + str_1[-1:]
print(str_1)

# Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.
str_2 = ['.html', '.kk', '.html']
html_list = [i for i in str_2 if i.endswith('.html')]
print(html_list)

# Округлите эти дроби до одного знака в дробной части.
lst_1 = [1.456, 2.135, 3.32, 3.1, 5.34]
round_list = [round(num, 1) for num in lst_1]
print(round_list)

dct_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
values_list = list(dct_1.values())
print(values_list, '\n')

# Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.
word_1 = 'asdf'
word_2 = 'fghj'
if word_1[-1:] == word_2[:1]:
    print('True', '\n')

# Дана некоторая строка. Найдите позицию третьего нуля в строке.
str_3 = '03000303'
count = 0
position = -1
for i, char in enumerate(str_3):
    if char == '0':
        count += 1
        if count == 3:
            position = i
            break
print(position)

# Дан список с числами. Удалите из него числа, состоящие более чем из трех цифр.
list_1 = [11, 332, 2354, 1]
list_2 = []
for i in list_1:
    if len(str(i)) <= 2:
        list_2.append(i)
print(list_2)

# Дана строка. Проверьте, что эта строка состоит только из цифр.
str_1 = '3433'
print(str_1.isdigit(), '\n')

# Проверьте, что все цифры этого числа больше нуля.
num = 12345
for i in str(num):
    if int(i) > 0:
        pass
    else:
        print(f"цифра {i} является 0")
print('ok')

# Проверьте, что все элементы первого списка есть во втором.
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [1, 2, 3]
print(set(list_1) >= set(list_2), '\n')

# Дана строка. Сделайте заглавной последнюю букву каждого слова в этой строке.
str_2 = 'сделайте заглавной последнюю букву каждого слова в этой строке'
words = str_2.split()
result = []
for word in words:
    result.append(word[:-1] + word[-1:].upper())
print(' '.join(result), '\n')

# Дана строка. Проверьте, что эта строка состоит только из четных цифр.
str_num = '2461'
num_even = True
for i in str_num:
    if int(i) % 2 != 0:
        num_even = False
        print(f"{i} не чётная цифра")
    elif int(i) % 2 == 0:
        print('Ok')

# Получите символы, которые есть и в одной, и в другой строке:
txt_1 = '12345'
txt_2 = '45678'
inter = ''.join(set(txt_1) & set(txt_2))
print(inter, '\n')

# Переведите в верхний регистр все подстроки, в которых количество букв меньше или равно трем. В нашем случае должно получится следующее: 'A BC DEF ghij'
low_str = 'a bc def ghij'
words_1 = low_str.split()
result_1 = []
for word in words_1:
    if len(word) <= 3:
        result_1.append(word.upper())
    else:
        result_1.append(word)
print(' '.join(result_1), '\n')

# Дан список с числами. Проверьте, что все числа из этого списка содержат в себе цифру 3.
num_list = [33, 93, 63]
num_3_list = all(str(num).count('3') > 0 for num in num_list)
print(num_3_list)

# Через запятую написаны числа. Получите максимальное из этих чисел.
num_1 = 11, 4, 43, 6
maximum = max(list(num_1))
print(maximum, '\n')

# Преобразуйте ее в формат: 'snake_case'
str_3 = 'kebab-case'
str_31 = 'snake_'.join(str_3.split('kebab-'))
print(str_31)

# Преобразуйте ее в формат: 'camelCase'
str_4 = 'snake_case'
str_41 = 'camelC'.join(str_4.split('snake_c'))
print(str_41)

# Преобразуйте ее в формат: 'snake_case'
str_5 = 'camelCase'
str_51 = 'snake_c'.join(str_5.split('camelC'))
print(str_51, '\n')

# Дан список с числами. Удалите из него числа, имеющие два и более нуля.
lst_3 = [100, 3000, 324]
filter_lst = [i for i in lst_3 if str(i).count('0') < 2]
print(filter_lst)

# Найдите все числа от 1 до 1000, сумма цифр которых равна 13. Результат запишите в сет.
set_num = set()

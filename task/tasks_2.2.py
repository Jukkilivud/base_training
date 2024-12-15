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
for i in range(1, 1001):
    if sum(int(i) for i in str(i)) == 13:
        set_num.add(i)
print(set_num, '\n')

# Сделайте так, чтобы в нем каждый элемент повторился два раза: [1, 1, 2, 2, 3, 3]
lst_4 = [1, 2, 3]
lst_41 = []
for i in lst_4:
    lst_41 += i, i
print(lst_41)

lst_41 = [i for i in lst_4 for _ in range(2)]
print(lst_41, '\n')

# Переберите эти списки одним циклом и в каждой итерации выводите их элементы следующим образом: '1,4' '2,5' '3,6'
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
for i, j in zip(lst1, lst2):
    print(f"{i},{j}")

# Дан список чисел и число. Оставьте в списке только те числа, которые являются делителями заданного числа.
num_2 = [3, 4, 6, 1, 8, 12, 11]
num_division = 2
filter_num = [i for i in num_2 if i % num_division == 0]
print(filter_num, '\n')

# Дан список с числами. После каждого однозначного числа вставьте еще такое же.
num_3 = [3, 4, 6, 1, 8, 12, 11, 7]
num_duble = [i for i in num_3 for _ in range(2) if len(str(i)) == 1]
print(num_duble, '\n')

# Даны два числа. Получите список цифр, которые есть и в одном, и во втором числе.
n = 1234
n2 = 3456
inter = set(str(n)).intersection(set(str(n2)))
print(list(inter))


def inter(n, n2):
    s = set(str(n))
    s2 = set(str(n2))
    return list(s.intersection(s2))


print(inter(1234, 3456), '\n')

# Дано число. Получите список позицией всех цифр 3 в этом числе, за исключением первой и последней.
n3 = 132303
positions = [i for i in range(1, len(str(n3)) - 1) if str(n3)[i] == '3']
print(positions)

# Дан список с числами. Оставьте в нем числа, состоящие из разных цифр, а остальные удалите.
lst3 = [11, 43, 44, 55, 934]
filter_lst2 = [num for num in lst3 if len(set(str(num))) == len(str(num))]
print(filter_lst2)

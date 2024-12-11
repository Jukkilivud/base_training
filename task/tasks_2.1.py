# С помощью включения создайте следующий список: [1, 2, 3, 4, 5, 6]
list_com = [i for i in range(1, 7)]
print(list_com, '\n')

# Объедините два списка в один
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2)

# Найдите сумму первой половины элементов этого списка.
lst_1 = [1, 2, 3, 4, 5, 6]
sum_list = sum(lst_1[:3])
print(sum_list)

# С помощью включения создайте следующий список: [1, 3, 5, 7, 9]
odd_nums = [i for i in range(1, 10, 2)]
print(odd_nums)

# Объедините эти кортежи в один:
tpl_1 = (1, 2, 3)
tpl_2 = (4, 5, 6)
print(tpl_1+tpl_2)

# Объедините эти словари в один:
dct1 = {'a': 1, 'b': 2, }
dct2 = {'c': 3, 'd': 4, }
dct1.update(dct2)
print(dct1)

# Поделите сумму первой половины элементов этого списка на сумму второй половины элементов.
list_1 = [1, 2, 3, 4, 5, 6]
one_half = sum(list_1[:3])
two_half = sum(list_1[3:])
division_list = two_half / one_half
print(division_list, '\n')

# Проверьте, что все цифры этого числа являются нечетными.
num_1 = 1357
for i in str(num_1):
    if int(i) % 2 != 0:
        print(f"Эта цифра в числе {num_1} является не чётной.")
    else:
        print(f"Эта цифра в числе {num_1} является чётной!")
print("Второй вариант решения с помощью генератора списков:")
s = [i for i in str(num_1) if int(i) % 2 != 0 and print('ok')]

# Проверьте, что это слово читается одинаково с любой стороны.
word = 'abcba'
if word == word[::-1]:
    print("Читается одинаково")

# Объедините эти сеты в один: {1, 2, 3, 4, 5, 6}
set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
set_1.update(set_2)
print(set_1)

# Дана строка. Удалите из нее все гласные буквы.
str_1 = 'asdfo'
vowels = 'aeoui'
str_1 = ''.join([char for char in str_1 if char.lower()not in vowels])
print(str_1)

# Получите сет их общих элементов:
st_1 = {1, 2, 3, 4, 5}
st_2 = {4, 5, 6, 7, 8}
st_total = st_1.intersection(st_2)
print(st_total)

# Получите сет элементов, входящих только в один из сетов:
st_diff = st_1.symmetric_difference(st_2)
print(st_diff)

# Дан текст со словами. Запишите в список все слова, начинающиеся на букву 'a'.
text_book = 'sdf affd aeew vv ajj'
text_list = []
for w in text_book.split():
    if w.startswith('a'):
        text_list.append(w)
print(text_list)

# Дан список с числами. Проверьте, что все элементы этого списка являются положительными числами.
list_numbers = [10, 11, -34, 4432, 16]
for i in list_numbers:
    if int(i) > 0:
        print('Ok')
    elif int(i) < 0:
        print(f"Ошибка, число: {i} является отрицательным!")

# Получите список их общих элементов:
lst_2 = [1, 2, 3, 4, 5]
lst_3 = [4, 5, 6, 7, 8]
st = set(lst_2) & set(lst_3)
print(list(st))

# Сделайте строку, содержащую столько нулей, сколько указано в переменной. В нашем случае получится такая строка:
num_2 = 5
print(str('0' * num_2))

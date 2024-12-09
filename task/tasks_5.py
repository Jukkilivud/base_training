# С помощью цикла заполните список целыми числами от 1 до 10.
list_1 = []
for i in range(1, 11):
    list_1.append(i)
s = ', '.join(map(str, list_1))
print(s, '\n')

# Дана строка с буквами. Проверьте, что в этой строке не более двух заглавных букв.
str_1 = 'asdFdsJff'
ss = ''
for i in str_1:
    if i == i.upper():
        ss += i
if len(ss) > 2:
    print(f"В строке {str_1} более двух заглавных букв: {ss}")
else:
    print(f"В строке {str_1} не более двух заглавных букв: {ss}")

# Преобразуйте элементы этого списка в числа:
list_2 = ['1', '2', '3', '4', '5']
list_num = [int(i) for i in list_2]
print(list_num, '\n')

# С помощью цикла заполните список четными числами из промежутка от 1 до 100.
even_number = []
for i in range(1, 101):
    if i % 2 == 0:
        even_number.append(i)
print(even_number)

# Выведите в консоль элементы этого списка в обратном порядке.
list_3 = [1, 2, 3, 4, 5]
print(list_3[::-1])

txt_1 = 'abcde'
txt_2 = '12345'
dict_txt = dict(zip(txt_1, txt_2))
print(dict_txt, '\n')

# Дана строка с буквами и цифрами. Проверьте, что в этой строке не более трех букв.
str_2 = 'ssjd324'
word = ''
for i in str_2:
    if i.isalpha():
        word += i
if len(word) <= 3:
    print('Good')
else:
    print('No')

# Дано число. Получите первую четную цифру с конца этого числа.
num_2 = 1468
s = str(num_2)
for i in reversed(s):
    if int(i) % 2 == 0:
        print(i)
        break

# Замените в ней первый символ каждого слова на '!':
str_3 = "abcde abcde abcde"
str_4 = str_3.replace('a', '!')
print(str_4, '\n')

# Найдите сумму элементов этого списка.
list_4 = ['1', '2', '3', '4', '5']
sum_list = 0
for i in list_4:
    sum_list += int(i)
print(sum_list)

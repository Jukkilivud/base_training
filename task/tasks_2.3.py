# Удалите из большего списка лишние элементы с конца так, чтобы длины списков стали одинаковыми.
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5, 7]
while len(lst1) != len(lst2):
    if len(lst1) > len(lst2):
        lst1.pop()
    else:
        lst2.pop()
print(lst1 == lst2, lst1, lst2, '\n')

# Напишите код, который перевернет числа в этом списке по следующему принципу: [321, 654, 987]
list_1 = [123, 456, 789]
reversed_list = [int(str(num)[::-1]) for num in list_1]
print(reversed_list, '\n')

# Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию.
num_1 = 1237
str_num = str(num_1)
for i in range(len(str_num) - 1):
    if str_num[i] >= str_num[i + 1]:
        print('no')
        break
else:
    print('good')

# Удалите из списка все пустые строки.
lst3 = [1, '', 2, 3, '', 5]
while '' in lst3:
    lst3.remove('')
print(lst3)

# Выведите в консоль все элементы этого списка.
lst4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for i in lst4:
    for j in i:
        print(j, end=' ')
    print()

# Дано число. Получите список делителей этого числа.
num_2 = 8
num_div = []
for i in range(1, num_2 + 1):
    if num_2 % i == 0:
        num_div.append(i)
print(num_div)

# Выведите в консоль все числа в промежутке от 10 до 1000, у которых первая цифра четная.
even_list = []
for i in range(10, 1001):
    if str(i)[0] in ['2', '4', '6', '8']:
        even_list.append(i)
print(even_list)

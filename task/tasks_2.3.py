# Удалите из большего списка лишние элементы с конца так, чтобы длины списков стали одинаковыми.
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
for i in lst1, lst2:
    if len(lst1) != len(lst2):
        lst2.pop()
print(lst1 == lst2, lst1, lst2)

# Напишите код, который перевернет числа в этом списке по следующему принципу: [321, 654, 987]
list_1 = [123, 456, 789]
reversed_list = [int(str(num)[::-1]) for num in list_1]
print(reversed_list)

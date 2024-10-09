a_set = {1, 'alex', 3.14}

print(a_set)
print(type(a_set), '\n')

# Добавление элементов в множество
a_set.add('Jukki')
print(a_set)

# Добавление нескольких элементов в множество
a_set.update(['and', 21, 88])
print(a_set, '\n')

# Удаление элементов из множества
a_set.remove(1)
print(a_set)

a_set.discard(88)
print(a_set)

a_set.pop()
print(a_set, '\n')

# print(dir(set), '\n')

# Функция вхождения во множество
one_set = {1, 2, 3, 4, 5}
two_set = {5, 6, 7, 8, 9}
print(7 in one_set)
print(7 in two_set)
print(len(one_set), '\n')

# Очистка множества (сперва сделаем копию)
a = two_set.copy()
a.clear()
print(a)

# two_set = {5, 6, 7, 8, 9}
print(two_set, '\n')

# Объединение множеств
tree_set = one_set | two_set
print(tree_set)
tree_set.clear()
tree_set = one_set.union(two_set)
print(tree_set, '\n')

# Пересечение множеств
tree_set.clear()
tree_set = one_set & two_set
print(tree_set)
tree_set.clear()
tree_set = one_set.intersection(two_set)
print(tree_set, '\n')

# Разность множеств (чем отличаются)
tree_set.clear()
tree_set = one_set - two_set
print(tree_set)
tree_set.clear()
tree_set = one_set.difference(two_set)
print(tree_set, '\n')

# Симметричная разность множеств (убирает символы которые есть в обоих множествах)
tree_set.clear()
tree_set = one_set ^ two_set
print(tree_set)
tree_set.clear()
tree_set = one_set.symmetric_difference(two_set)
print(tree_set, '\n')

# Подмножество и надмножество
a = {1, 2, 3, 4, 5, 6, 7}
b = {1, 2, 3, 4, 5, 6, 7}
c = a <= b  # b является подмножеством a
print(c)
c = a.issubset(b)
print(c, '\n')


a = {1, 2, 3, 4, 5, 6, 7}
b = {1, 2, 3}
c = a >= b  # a является надмножеством b
print(c)
c = a.issuperset(b)
print(c, '\n')
# Полное удаление множества из памяти
# del two_set
# print(two_set)

# Как убрать повторяющиеся элементы из списка, строки и кортежа
a_list = [1, 2, 2, 2, 3]
a_set = set(a_list)
a_list = list(a_set)
print(a_list)

a_str = '1', '2', '2'
b_set = set(a_str)
a_str = str(b_set)
print(a_str)

a_tuple = (1, 2, 3, 3, 3)
c_set = set(a_tuple)
a_tuple = tuple(c_set)
print(a_tuple)

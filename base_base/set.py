a_set = {1, 'alex', 3.14}

print(a_set)
print(type(a_set))

# Добавление элементов в множество
a_set.add('Jukki')
print(a_set)

# Добавление нескольких элементов в множество
a_set.update(['and', 21, 88])
print(a_set)

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

# Очистка множества
two_set.clear()
print(two_set)

two_set.update([5, 6, 7, 8, 9])
print(two_set)

# del two_set
# print(two_set)

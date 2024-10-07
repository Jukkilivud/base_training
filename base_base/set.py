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

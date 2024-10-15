a_list = ['apple', 'candy', 'pens', 'notepad']
print(a_list)
a_list[1] = 'candy melon'
print(a_list)
a_list[-1] = 'book'
print(a_list)
sub_list = [['apple', 'banana'], ['pens', 'book']]
print(sub_list, '\n')

# Перебор списков в цикле.
for i in a_list:
    print(i)

for i in a_list:
    if 'apple' in i:
        print('\n', True)

# Срезы списков.
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = b_list[:5]
b = b_list[5:]
c = b_list[:10:2]
print(a, b, c)

# Операции со списками
print(len(b_list))
print(min(b_list))
print(max(b_list))
c_list = a_list + b_list + ["fuck you!"]
print(c_list, '\n')

# Методы списков
удаляет_последний_элемент = b_list.pop()
print(удаляет_последний_элемент)
print(b_list)

удаление_по_индексу = b_list.pop(0)
print(удаление_по_индексу)
del a_list[0]
a_list.remove('pens')
print(a_list)


b_list.append(10)
print(b_list)
b_list.extend([5, 5, 1, 0.5, 2.5])
print(b_list)
print(sorted(b_list))
b_list.sort(reverse=True)
print(b_list)

print(b_list.count(5))

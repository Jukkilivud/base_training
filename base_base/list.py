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

print('\n'*2)

print('Jukki'.center(49, '*'), '\n')


a_string = 'Alex'
a_string_2 = 'Jukki'
print(a_string + ' ' + a_string_2)
print('fuck ' * 3)
print(len('fuck'))

# Доступ по индексу
s = a_string
print(s[0])
print(s[-1])

# Срез
x = a_string_2
print(x[:])
print(x[0:1])
print(x[2:4])
print(x[::2])
print(x[::-2])
print(x[:2])
print(x[2:], '\n')


word = a_string.isalpha()
print(word)
word_2 = 'Alex'.isalpha()
print(word_2)
print(x.endswith('kki'))
print(x.startswith('J'), '\n')

a_str = "hello my people"
print(a_str.title())
print(a_str.capitalize())
print(a_str.istitle())
print(a_str.upper())

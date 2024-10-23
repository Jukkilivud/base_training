a_dict = {'name': 'Alex',
          'nick': 'Jukki',
          'age': 36,
          'working': 'glass_installer', }
print(a_dict)
print(type(a_dict))

# Генератор словарей
a = {x: x*2 for x in range(5)}
print(a, '\n')

d = a_dict
print(d.items())
print(d.keys())
print(d.values())
print(d.setdefault('name'))
print(d.setdefault('nick', 'fuck off'))
print(d.setdefault('nicka', 'fuck off'))

# Обновление, добавление в словарь
s = {'many': 100}
d.update(s)
print(d)

print(len(d))

d.clear()
print(d)

# 1
x = [1, 'основной_список', ['вложенный_список', 4], 5, 6]
print(x[1])
print(x[2][0], '-----------------------------------')

# 2
print(issubclass(bool, int))
print(isinstance(True, bool))
print(isinstance(False, bool))
print(True+False)

a = None
a = 100
print(a)

# 3


def ing(i):
    if isinstance(i, int):
        i += 1
    elif isinstance(i, str):
        i = int(i)
        i += 1
    return i


x = ing(5)
x1 = ing('7')
print(x, x1)

# 4
a = '12.345'
a = float(a)
a = int(a)
print(a)

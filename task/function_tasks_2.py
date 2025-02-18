data_for = '2025-12-31'
y, m, d = data_for.split('-')
date_dict = {'y': y, 'm': m, 'd': d, }
print(date_dict)

a = set(date_dict.values())
print(a)


def position(st: str):
    pos = -1
    for i, char in enumerate(st):
        if char.isdigit():
            pos = i
            break
    print(f"Позиция первой цифры: {pos}", end=' ')


position('ads3dj')
position('abc10dfdf4')


def even_num(num: int) -> int:
    count = 0
    for i, char in enumerate(str(num)):
        if char.isdigit():
            if int(char) % 2 == 0:  # Все чётные цифры.
                count += 1
    print(f"Количество чётных цифр в числе {num} = {count}.")


even_num(12345678)
even_num(68)
even_num(1000)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
# key = dict1.keys()
print(list(dict1.keys()))


def unever(str1: str) -> str:
    result = ''
    for i in range(len(str1)):
        if i % 2 == 0:
            result += str1[i].upper()  # в верхний регистр все нечетные буквы
        else:
            result += str1[i].lower()
    print(result)


unever('abcde')
unever('aCbDcde')

str2 = 'aaa bbb ccc'
print(str2.title())

date = '2025-12-31'
date = date.split('-')
print(tuple(date))


def zero(str1: str):
    count = 0
    for i, char in enumerate(str1):
        if char == '0':
            count += 1
    print(count)


zero('023m0df0dfg0')


def three(str1: str) -> str:
    for i in range(2, len(str1), 3):
        str1 = str1[:i] + str1[i+1:]
    return str1


print(three('abcdefg'))


def division_element(lis: list) -> float:
    t = 0
    f = 0
    for i, char in enumerate(lis):
        if i % 2 == 0:
            f += char
        if i % 2 != 0:
            t += char
    return f/t


print(division_element([1, 2, 3, 4, 5, 6]))

print(9/12)

_ = ['2025', '12', '31']
print(tuple(_))


def num_str(str1: str) -> list:
    list_num = []
    for i, char in enumerate(str1):
        if str(char).isdigit():
            list_num += str(i)
    return list_num


print(num_str('1a1b2j1'))


def title_word(str1: str) -> str:
    word = str1.swapcase()
    return word


s = title_word('AbCdE')
print(s)

ss = [1, 2, 3, 4, 5, 6]
ss1 = str(ss).split(', ')
print(ss1[0]+ss1[1]+', ' + ss1[2]+ss1[3] + ', ' + ss1[4]+ss1[5])

ss = [1, 2, 3, 4, 5, 6]
ss_pairs = [int(str(a) + str(b)) for a, b in zip(ss[::2], ss[1::2])]
print(ss_pairs)


def title_two(jk: str) -> str:
    r = jk.split(' ')
    for i in range(1, len(r), 2):
        r[i] = r[i].title()
    return ' '.join(r)


x = title_two('aaa bbb ccc ddd eee')
print(x)


def titlee(jk: str) -> str:
    if jk.istitle():
        print('Upper')
    else:
        print('Lower')


titlee('a')
titlee('A')


def nuum(n: int) -> int:
    nm = ''
    for i in str(n):
        if int(i) % 2 == 0:
            nm += i
    return f"В числе {n} количество чётных цифр = {nm}"


print(nuum(1234598))
print(nuum(1357))


dict1 = ('2025', '12', '31')
dic = {k: v for k, v in zip(['year', 'month', 'day'], dict1)}
print(dic)

list1 = []
for i in range(1, 11):
    list1.append(i)
print(list1)


def title2(str12: str):
    count = 0
    for char in str12:
        if char.isupper():
            count += 1
            if count > 2:
                return False
    return True


print(title2('asdJjKjJK'))
print(title2('asdJjG'))

listt = ['1', '2', '3', '4', '5']
li = [int(num) for num in listt]
print(li)
print(li[::-1])

even = [num for num in range(1, 100) if num % 2 == 0]
print(even)

txt1 = 'abcde'
txt2 = '12345'
dict1 = {k: v for k, v in zip(txt1, txt2)}
print(dict1)


def num_word(st: str) -> str:
    word = sum(1 for i in st if i.isalpha())
    print('\n', word)
    if word <= 3:
        return f'Меньше 3х букв: {word} буквы.'
    else:
        return f'Больше 3х букв: {word} буквы.'


x1 = num_word('asd222')
x11 = num_word('2kdssdd1')
print(x1)
print(x11)


def odd_num(numbers: int) -> int:
    try:
        numbers = str(numbers)
        odd = []
        for i in numbers:
            if int(i) % 2 == 0:
                odd.append(i)
        return odd[-1]
    except:
        return f'{'<<numbers>>'} Передайте в функцию число, а не строку и прочую поебистику!!!'


x2 = odd_num(1345678)
x22 = odd_num(2466664)
x222 = odd_num('asdf')

print(x2, x22, x222)


string1 = 'abcde abcde abcde'
replace = string1.replace('a', '!')
print(replace)
print(type(replace))


list2 = ['1', '2', '3', '4', '5']
summ = 0
for i in list2:
    summ += int(i)
print(f"Сумма списка {list2} равна {summ}.")

new_list = [i for i in range(1, 10, 2)]
print(new_list)

tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
print(tpl1 + tpl2)

dct1 = {'a': 1, 'b': 2, }
dct2 = {'c': 3, 'd': 4, }
dct1.update(dct2)
print(dct1)


def uneven(nums: int) -> bool:
    nums = str(nums)
    """Посдсчёт нечётных элементов в числе. Если счётчик больше единицы, значит в числе есть нечётные элементы. Иначе все элементы в числе чётные."""
    count = 0
    try:
        for i in nums:
            if int(i) % 2 != 0:
                count += int(i)
                if count > 0:
                    # Надо решить, почему останавливается на первой проверки элемента! Сделать вывод всех нечётных элементов!
                    return False, f'{count}'
        return True, f"{count}"
    except:
        return f"\nВместо {nums} введите в функцию число!"


z1 = uneven(13579)
z2 = uneven(24680)
z3 = uneven('asdf')
print(z1, z2, z3)

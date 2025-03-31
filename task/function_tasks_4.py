def palindrome(word: str) -> str:
    try:
        if word == word[::-1]:
            return f"Слово '{word}' является палиндромом."
        else:
            return f"Слово '{word}' не является палиндромом."
    except TypeError:
        return f"{word}....Введите слово"


pal = palindrome('alla')
print(pal)
pal1 = palindrome('alsdla')
print(pal1)
pal2 = palindrome(41234)
print(pal2)

print('\n')


def n_sum(n: int) -> int:
    s = n + (n+n) + (n+n+n)
    return s


f = n_sum(5)
print(f)


def stop_237(txt: list) -> list:
    """Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237."""
    even_number = []
    for i in txt:
        if i % 2 == 0:
            even_number.append(i)
        if i == 237:
            break
    return even_number


num_list = stop_237([2, 23, 26, 344, 237, 4, 24])
print(num_list)

print('\n')


def latin_text(leng: int) -> str:
    """Сделайте функцию, которая сгенерирует строку заданной длины, заполненную случайными латинскими буквами."""
    import string
    import random
    abc_alphabet = string.ascii_letters
    # Мини генератор паролей!!!!!!!!!!!!!!!!!!!!!!
    return ' '.join(random.sample(abc_alphabet, leng))


a1 = latin_text(10)
print(a1)


def upper_text(txt: str) -> str:
    """Сделайте функцию, которая параметром будет получать строку со словами, а возвращать строку в верхнем регистре, состоящую из первых букв слов."""
    str_upper = ''
    for i in txt.split():
        str_upper += (i[:1]).upper()
    print(len(str_upper))  # Счётчик слов в тексте
    return str_upper  # Возвращает первые буквы слов в верхнем регистре.


a2 = upper_text("Сделайте функцию, которая параметром будет получать строку со словами, а возвращать строку в верхнем регистре, состоящую из первых букв слов.")
print(a2)

print('\n')


def division_list(lst_num: list) -> list:
    """Сделайте функцию, которая параметром будет принимать список с числами и заменять каждое число на список его делителей."""
    div_list = [[j for j in range(1, i+1) if i % j == 0] for i in lst_num]
    return div_list


dl = division_list([12, 6])
print(dl)
d2 = division_list([12, 6, 122])
print(d2)


def sorted_text(txt: str) -> str:
    """Сделайте функцию, которая параметром будет принимать текст со словами, а возвращать текст, в котором эти слова будут отсортированы в алфавитном порядке."""
    tx = txt.lower()
    tx = sorted(tx.split(' '))
    return ' '.join(tx)


print('\n')

txt_1 = sorted_text(
    "Сделайте функцию, которая параметром будет принимать текст со словами, а возвращать текст, в котором эти слова будут отсортированы в алфавитном порядке.")
print(txt_1)

print('\n')


def total_list(txt: list, txt2: list) -> list:
    """Сделайте функцию, которая параметром будет принимать два списка и возвращать список их общих элементов."""
    new_list = set(txt) & set(txt2)
    return list(new_list)


tot = total_list(['привет'], ['привет', 'всем'])
print(tot)
tot1 = total_list([1, 2, 3, 4], [1, 2, 3, 34, 23])
print(tot1)


def random_num(nums1: int, nums2: int) -> int:
    """Сделайте функцию, которая будет возвращать случайное число. Функция не должна возвращать одно и тоже число два раза подряд."""
    import random
    last_num = None
    while True:
        num = random.randint(nums1, nums2)
        if num != last_num:
            last_num = num
            return num


r = random_num(1, 3)
print(r)


def list_element(lst: list, elem: int) -> str:
    """Сделайте функцию, которая параметром будет принимать список и элемент и возвращать следующий за ним элемент."""
    for i in range(len(lst)):
        if lst[i] == elem:
            if i < len(lst) - 1:
                return lst[i+1]
            else:
                return lst[0]


ele = list_element([1, 22, 33, 44, 54], 54)
print(f"Следующий элемент {ele}")
ele2 = list_element([1, 22, 33, 44, 54], 33)
print(f"Следующий элемент {ele2}")

print('\n')


def list_random_elem(lst: list) -> int:
    """Сделайте функцию, которая параметром будет принимать список и возвращать случайный элемент этого списка."""
    import random
    return random.choice(lst)


r1 = list_random_elem([1, 435, 45, 978, 11, 15, 19])
print(r1)


def list_random_more(lst: list) -> list:
    import random
    """Сделайте функцию, которая параметром будет принимать список и возвращать список из N случайных элементов этого списка."""
    return random.choices(lst, k=3)


more = list_random_more([1, 12, True, 35, 'asd', 93, 234, 567])
print(more)


def list_random_nodouble(lst: list) -> str:
    """Сделайте функцию, которая параметром будет принимать список и возвращать случайный элемент этого списка так, чтобы одинаковые элементы не возвращались два раза подряд."""
    import random
    last_num = None
    while True:
        nodouble = random.choice(lst)
        if nodouble != last_num:
            last_num = nodouble
            return nodouble


r2 = list_random_nodouble([1, 12, True, 35, 'asd', 93, 234, 567])
print(r2)


def list_simple(start: int, end: int) -> list:
    """Сделайте функцию, которая будет возвращать список простых чисел из заданного промежутка."""
    list_s = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                list_s.append(num)
    return list_s


simple = list_simple(1, 100)
print(f"Простые числа: {simple}")


def more_nums(*args: int) -> int:
    """Сделайте функцию, которая параметрами будет принимать любое количество чисел, а возвращать их сумму."""
    return sum(args)


more2 = more_nums(10, 30, 1, 2, 3)
print(more2)


def list_no_double(start: int, end: int, N: int) -> list:
    """Сделайте функцию, которая заполнит список N случайными числами из заданного промежутка так, чтобы в списке не было подряд двух одинаковых чисел."""
    import random
    result_N = []
    last = None
    while len(result_N) < N:
        num = random.randint(start, end)
        if num != last:
            result_N.append(num)
            last = num
    return result_N


s = list_no_double(1, 10, 5)
print(s)


def list_n(start: int, end: int, n: int) -> list:
    """Сделайте функцию, которая заполнит список N случайными числами из заданного промежутка так, чтобы числа не повторялись."""
    import random
    if end - start + 1 < n:
        raise ValueError(
            "Диапазон слишком мал для запрашиваемого количества уникальных чисел.")
    result = set()
    while len(result) < n:
        number = random.randint(start, end)
        result.add(number)

    return list(result)


double_no = list_n(1, 10, 5)
print(double_no)
# double_no2 = list_n(1, 2, 5)
# print(double_no2)

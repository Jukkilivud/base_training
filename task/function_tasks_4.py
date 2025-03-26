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
    # Мини генератор паролей
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


def division_list(lst_num: list) -> list:
    """Сделайте функцию, которая параметром будет принимать список с числами и заменять каждое число на список его делителей."""
    for i in lst_num:
        pass

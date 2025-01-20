# Дано число. Проверьте, что у этого числа есть только один делитель, кроме него самого и единицы.
num = 5
if num % 1 == 0 and num % num == 0:
    print('true')

# Выведите в консоль все числа в промежутке от 10 до 1000, у которых предпоследняя цифра четная.
for num in range(10, 100):
    last_digit = num % 10
    # извлекает последнюю цифру. Например, если num // 10 равно 12, то (num // 10) % 10 будет равно 2.
    second_last_digit = (num // 10) % 10
    if second_last_digit % 2 == 0 and second_last_digit > 1:
        print(num)

# Разбейте эту строку в список так, чтобы каждая непустая линия текста стала отдельным элементом списка:
str1 = '''
    text1
    text2
    text3
    text4
    text5
    '''
lst1 = str1.split("'''")
# lst1 = [s.strip() for s in str1 if s.strip()]
lst2 = '\n'.join(lst1)
print((lst2))

def email(pochta: str) -> bool:
    mail = ['gmail.com', 'mail.ru', 'ya.ru']
    if pochta.endswith(tuple(mail)):
        return True
    else:
        return False


m = email('sadf@gmail.com')
print(m)
m1 = email('sadf@gail.com')
print(m1)
m2 = email('sadf@ya.ru')
print(m2)


def merge(lst: list) -> list:
    merge_list = []
    for i in lst:
        for o in str(i):
            merge_list.append(int(o))
    return merge_list


sp = merge([123, 456, 789])
print(sp)


def user_tel(number: int) -> str:
    # try:
    if len(str(number)) == 11 and str(number)[0] == '8':
        return f"Номер {number} принят"
    if len(str(number)) != 11:
        return "Введите корректный, 11-ти значный, номер телефона"
    if str(number)[0] != '8':
        return "Набор номера через 8"
    # except Exception:
    #     return "Ваш номер не будет зарегистрирован!"


telephone = user_tel(89130331212)
print(telephone)
telephone1 = user_tel(32922331212)
print(telephone1)
telephone2 = user_tel(8882922331212)
print(telephone2)

print('\n')


def medium_num(*args: int) -> int:
    medium_total = []
    medium_total.append(args)
    print(medium_total)
    sum_medium = sum(args) / len(args)
    return f"Средне арифметическое введённых чисел равно: {int(sum_medium)}"


num_user = medium_num(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(num_user)
num_user01 = medium_num(10, 10, 100, 40)
print(num_user01)


def sum_digit(num: int) -> str:
    list_01 = str(num)
    if len(list_01) == 6:
        return f"Сумма пар чисел {num} равна: {int(list_01[:2]) + int(list_01[2:4]) + int(list_01[4:6])}"
    if len(list_01) < 5:
        return f"Что-то пошло не так..."


digits = sum_digit(123456)
print(digits)
digits1 = sum_digit(3456)
print(digits1)

str_01 = "Дана строка со словами. Отсортируйте слова в алфавитном порядке."
str_sorted = str_01.lower()
str_sorted = str_sorted.split()
print(sorted(str_sorted))

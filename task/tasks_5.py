# С помощью цикла заполните список целыми числами от 1 до 10.
list_1 = []
for i in range(1, 11):
    list_1.append(i)
s = ', '.join(map(str, list_1))
print(s, '\n')

# Дана строка с буквами. Проверьте, что в этой строке не более двух заглавных букв.
str_1 = 'asdFdsJff'
ss = ''
for i in str_1:
    if i == i.upper():
        ss += i
if len(ss) > 2:
    print(f"В строке {str_1} более двух заглавных букв: {ss}")
else:
    print(f"В строке {str_1} не более двух заглавных букв: {ss}")

# Преобразуйте элементы этого списка в числа:
list_2 = ['1', '2', '3', '4', '5']
list_num = []
# for i in list_2:
#     if i == int(i):
#         list_num += int(i)
print(list_num)

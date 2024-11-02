print("Program started")
try:
    print("Opening file...")
    a = open("README.tt", 'r')
    print(*a)
except:
    print("Данный файл не найден!" + " File not found!")
print("Program finished", '\n')


print("Program started")
try:
    print("Opening file...")
    a = open("README.tt", 'r')
    print(*a)
except FileNotFoundError:
    print("Данный файл не найден!" + " File not found!")
except Exception:
    print("Что-то пошло не так..." + " Something gone wrong...")
print("Program finished", '\n')


# Открытие файла и запись в него
print("Program started")
try:
    print("Opening file...")
    a = open("README.txt", 'r+')
    print(*a)
    try:
        print("Запись в файл" + " Writing to file...")
        a.write("Нужно же что-то добавить :)) ")
    except Exception:
        print("Что-то пошло не так..." + " Something gone wrong...")
    else:
        print("Успешно" + ' Success')
except FileNotFoundError:
    print("Данный файл не найден!" + " File not found!")
print("Program finished", '\n')

# Открытие файла и запись в него + finally
print("Program started")
try:
    print("Opening file...")
    a = open("README.txt", 'r+')
    print(*a)
    try:
        print("Запись в файл" + " Writing to file...")
        a.write("файналли в городе!! ")
    except Exception:
        print("Что-то пошло не так..." + " Something gone wrong...")
    else:
        print("Успешно" + ' Success')
    finally:
        print("Закрыть файл" + " Closing file...")
        a.close()
except FileNotFoundError:
    print("Файл не найден!" + "File not found!")
print("Program finished", '\n')

# Конструкция with/as которая не требует указывать закрытие файла .close()
# Некорректно работает, надо исправить
print("Program started")
try:
    print("Запись в файл" + " Writing to file...")
    with open('README.txt', 'r+') as q:
        q.write(" Использование конструкции with/as...")
except Exception:
    print("Что-то пошло не так..." + " Something gone wrong...")
print("Program finished")

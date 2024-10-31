print("Program started")
try:
    print("Opening file...")
    f = open("README.tt", 'r')
    print(*f)
except:
    print("Данный файл не найден!" + " File not found!")
print("Program finished", '\n')


print("Program started")
try:
    print("Opening file...")
    f = open("README.tt", 'r')
    print(*f)
except FileNotFoundError:
    print("Данный файл не найден!" + " File not found!")
except Exception:
    print("Что-то пошло не так..." + " Something gone wrong...")
print("Program finished", '\n')


# Открытие файла и запись в него
print("Program started")
try:
    print("Opening file...")
    f = open("README.txt", 'r+')
    print(*f)
    try:
        print("Запись в файл" + " Writing to file...")
        f.write("  Нужно же что-то добавить :))")
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
    z = open("README.txt", 'r+')
    print(*z)
    try:
        print("Запись в файл" + " Writing to file...")
        z.write("файналли в городе!!")
    except Exception:
        print("Что-то пошло не так..." + " Something gone wrong...")
    else:
        print("Успешно" + ' Success')
    finally:
        print("Закрыть файл" + " Closing file...")
        z.close()
except FileNotFoundError:
    print("Файл не найден!" + "File not found!")
print("Program finished", '\n')

# Конструкция with/as которая не требует указывать закрытие файла .close()
print("Program started")
try:
    print("Запись в файл" + " Writing to file...")
    with open('README.txt', 'r+') as x:
        x.write(" Использование конструкции with/as...")
except Exception:
    print("Что-то пошло не так..." + " Something gone wrong...")
print("Program finished")

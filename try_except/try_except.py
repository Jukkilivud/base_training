# -*-coding:cp1251-*-

print("Program started")
try:
    print("Opening file...")
    f = open("README.tt", 'r')
    print(*f)
except:
    print("Данный файл не найден!" + " File not found!")
finally:
    x = open("try_except\README.txt", 'r')
    print(*x)
    x.close()
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
finally:
    x = open("try_except\README.txt", 'r')
    print(*x)
    x.close()
print("Program finished", '\n')


print("Program started")
try:
    print("Opening file...")
    f = open("try-except\README.txt", 'r+')
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
finally:
    x = open("try_except\README.txt")
    print(*x)
    x.close()
print("Program finished")

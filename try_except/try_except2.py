# Конструкция with/as которая не требует указывать закрытие файла .close()
print("Program started")
try:
    print("Запись в файл" + " Writing to file...")
    with open('README.txt', 'r+') as f:
        f.write(" Использование конструкции" + " with/as..")
except Exception:
    print("Что-то пошло не так..." + " Something gone wrong...")
print("Program finished")

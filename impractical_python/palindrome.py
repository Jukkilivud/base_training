import sys


def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{} \nОшибка при открытии {}. Завершение программы.".format(
            e, file), file=sys.stderr)
        sys.exit(1)


f = load('impractical_python\dicts.txt')
print(f)

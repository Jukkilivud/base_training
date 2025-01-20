from collections import Counter
from typing import Union

try:
    stocks = {
        'GOOG': (1235.20, 1242.54, 1231.06),
        'MSFT': (110.41, 110.45, 109.84),
    }
    print(stocks['GOOG'])
    print(stocks['MSFT'])
    print(stocks['MFT'])
except KeyError:
    print("Ну ты и дятел, нет такого ключа!!", '\n')

stocks = {
    'GOOG': (1235.20, 1242.54, 1231.06),
    'MSFT': (110.41, 110.45, 109.84),
}
print(stocks.get('OG'))
print(stocks.get('OG', 'Not Found'), '\n')


def letter_counter(sentence: str) -> Counter[str]:
    return Counter(sentence)


a = letter_counter('сколько_раз_встречается_буква_в_предложении')
print(a)

# Получение хеша объекта.
help(hash)
a = (101, 11)
b = '11, 3456, 8634'  # Хеш строки будет постоянно разный.
c = 111
print(hash(a))
print(hash(b))
print(hash(c))

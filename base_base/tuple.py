a_tuple = (4, 1, 9, 5, 6)
print(sorted(a_tuple))
b_tuple = (3.5, "normal", None, True)
c_tuple = (('one', 'two'), ['tree', 'four'], {
           'five': 'six'}, (('seven', 'eight'), ('nine', 'ten')))
print(b_tuple)
print(c_tuple)

# Смена значений переменных
x = 100
y = 200
x, y = y, x
print(x)
print(y)


def get_status(service_name):
    return None, f"service {service_name} is OK"


error, message = get_status('nginx')
print(error)
print(message)

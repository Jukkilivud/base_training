class Dog:
    name = None
    age = None
    breed = None

    def __init__(self, name, age, breed=None) -> None:       # Конструктор
        self.name_dog(name, age, breed)         # Установка данных
        self.get_dog()                          # Вывод данных

    def name_dog(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed

    def get_dog(self) -> None:
        print(self.name, 'Возраст:', self.age,
              'И порода:', self.breed, '\n')


x = Dog('Dog1', 3)
x2 = Dog('Dog2', 2, 'chehh')

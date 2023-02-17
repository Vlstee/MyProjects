class Animal:
    def __init__(self, type_animal, name):
        self.type_animal = type_animal
        self.name = name

    def info_name(self):
        print(f'Я {self.type_animal} по имени {self.name}')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__('кошка', name)
        self.name = name
        self.age = age

    def info(self):
        print(f'Мне {self.age} годика')

    def sound(self):
        print('---Мяу---')


class Dog(Animal):
    def __init__(self, name, age):
        super(). __init__('собака', name)
        self.name = name
        self.age = age

    def info(self):
        print(f'Мне {self.age} годика')

    def sound(self):
        print('---Гав---')


cat = Cat('Снежок', 3)
dog = Dog('Шарик', 4)

for animal in (cat, dog):
    animal.info_name()
    animal.info()
    animal.sound()

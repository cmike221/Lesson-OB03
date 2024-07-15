class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def move(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "чирикающий"

    def move(self):
        return "летать"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "рычащий"

    def move(self):
        return "ходить"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "шипящий"

    def move(self):
        return "ползать"


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} делает {animal.make_sound()} звук.")

# Пример использования классов и функции animal_sound
parrot = Bird("Попугай", 2, 0.5)
lion = Mammal("Лев", 5, "золотой")
snake = Reptile("Змея", 3, "гладкая")

animals = [parrot, lion, snake]

animal_sound(animals)

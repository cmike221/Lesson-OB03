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

# Пример использования классов
parrot = Bird("Попугай", 2, 0.5)
print(f"{parrot.name} издает {parrot.make_sound()} звук и может {parrot.move()}.")

lion = Mammal("Лев", 5, "золотой")
print(f"{lion.name} издает {lion.make_sound()} звук и может {lion.move()}.")

snake = Reptile("Змея", 3, "гладкий")
print(f"{snake.name} издает {snake.make_sound()} звук и может {snake.move()}.")

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
        return "чирикать"

    def move(self):
        return "летать"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "рычать"

    def move(self):
        return "ходить"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "шипеть"

    def move(self):
        return "ползать"


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} работает в качестве {self.position}"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Можно добавлять только животных")

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise ValueError("Можно добавлять только сотрудников")

    def get_animals(self):
        return [animal.name for animal in self.animals]

    def get_employees(self):
        return [employee.name for employee in self.employees]


# Пример использования классов и класса Zoo
parrot = Bird("Попугай", 2, 0.5)
lion = Mammal("Лев", 5, "золотой")
snake = Reptile("Змея", 3, "гладкий")

zookeeper = Employee("Оксана", "Zookeeper")
guide = Employee("Михаил", "Guide")

zoo = Zoo("Гороодском зоопарке")
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_employee(zookeeper)
zoo.add_employee(guide)

print(f"Животные в {zoo.name}: {zoo.get_animals()}")
print(f"Сотрудники в {zoo.name}: {zoo.get_employees()}")

import pickle

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

class ZooKeeper(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal}.")

class Veterinarian(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal}.")

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

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Создается новый зоопарк.")
            return cls("Новый Зоопарк")

# Пример использования классов и класса Zoo
if __name__ == "__main__":
    zoo = Zoo.load_from_file("zoo_data.pkl")

    parrot = Bird("Попугай", 2, 0.5)
    lion = Mammal("Лев", 5, "золотой")
    snake = Reptile("Змея", 3, "гладкий")

    zookeeper = ZooKeeper("Оксана", "смотритель")
    guide = Employee("Михаил", "шеф")
    veterinarian = Veterinarian("Мария", "ветеринар")

    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    zoo.add_employee(zookeeper)
    zoo.add_employee(guide)
    zoo.add_employee(veterinarian)

    print(f"Животные в {zoo.name}: {zoo.get_animals()}")
    print(f"Сотрудники в {zoo.name}: {zoo.get_employees()}")
    zookeeper.feed_animal("Попугая")
    veterinarian.heal_animal("Льва")

    zoo.save_to_file("zoo_data.pkl")

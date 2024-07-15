class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self, food: str):
        print(f"{self.name} кушает {food}")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Гав!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")

# Пример использования подклассов
if __name__ == "__main__":
    dog = Dog(name="Барра", age=5)
    cat = Cat(name="Аврора", age=3)

    print(dog)
    dog.make_sound()
    dog.eat("кости")

    print(cat)
    cat.make_sound()
    cat.eat("рыбу")

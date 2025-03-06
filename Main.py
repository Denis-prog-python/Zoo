class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")

    def eat(self):
        print(f"{self.name} ест.")

# Пример использования класса Animal
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} лает!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} Мяукает!")

# Создаем экземпляры классов
dog = Dog("Шарик", 3)
cat = Cat("Муся", 5)

# Вызываем методы
dog.make_sound()  # Шарик лает!
cat.make_sound()  # Муся мяукает!

dog.eat()  # Шарик ест.
cat.eat()  # Муся ест.
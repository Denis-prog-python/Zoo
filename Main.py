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

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan  # Размах крыльев

    def make_sound(self):
        print(f"{self.name} чирикает!")

    def fly(self):
        print(f"{self.name} летает с размахом крыльев {self.wingspan} метра.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Цвет шерсти

    def make_sound(self):
        print(f"{self.name} рычит!")

    def run(self):
        print(f"{self.name} бежит.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Тип чешуи

    def make_sound(self):
        print(f"{self.name} шипит!")

    def crawl(self):
        print(f"{self.name} ползёт.")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создаем объекты
bird = Bird("Воробушек", 2, 0.1)
mammal = Mammal("Лео", 5, "Рыжий")
reptile = Reptile("Гена", 3, "Гладкий")
dog = Dog("Шарик", 3)
cat = Cat("Муся", 5)

# Создаем список животных
animals = [bird, mammal, reptile, dog, cat]

# Вызываем функцию animal_sound
animal_sound(animals)

# Вызываем методы для каждого животного
bird.fly()         # Воробушек летает с размахом крыльев 0.1 метра.
mammal.run()       # Лео бежит.
reptile.crawl()    # Гена ползёт.
dog.eat()          # Шарик ест.
cat.eat()          # Муся ест.
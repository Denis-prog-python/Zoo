class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")

    def eat(self):
        print(f"{self.name} ест.")

# Примеры использования класса Animal
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

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} ({self.position}) работает.")

class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.employees = []  # Список сотрудников в зоопарке

    def add_animal(self, animal):
        """Добавляет животное в зоопарк."""
        self.animals.append(animal)
        print(f"{animal.name} добавлен(а) в зоопарк.")

    def add_employee(self, employee):
        """Добавляет сотрудника в зоопарк."""
        self.employees.append(employee)
        print(f"{employee.name} ({employee.position}) добавлен(а) в зоопарк.")

    def show_animals(self):
        """Выводит список всех животных в зоопарке."""
        if not self.animals:
            print("В зоопарке пока нет животных.")
        else:
            print("Животные в зоопарке:")
            for animal in self.animals:
                print(f"- {animal.name} ({animal.__class__.__name__})")

    def show_employees(self):
        """Выводит список всех сотрудников в зоопарке."""
        if not self.employees:
            print("В зоопарке пока нет сотрудников.")
        else:
            print("Сотрудники в зоопарке:")
            for employee in self.employees:
                print(f"- {employee.name} ({employee.position})")

# Пример использования
zoo = Zoo()

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создаем животных
bird = Bird("Воробушек", 2, 0.1)
mammal = Mammal("Лео", 5, "Рыжий")
reptile = Reptile("Гена", 3, "Гладкий")
dog = Dog("Шарик", 3)
cat = Cat("Муся", 5)

# Создаем список животных
animals = [bird, mammal, reptile, dog, cat]

# Создаем сотрудников
employee1 = Employee("Иван", "Смотритель")
employee2 = Employee("Мария", "Ветеринар")

# Добавляем животных и сотрудников в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_employee(employee1)
zoo.add_employee(employee2)

# Вызываем функцию animal_sound
animal_sound(animals)

# Выводим информацию о зоопарке
zoo.show_animals()
zoo.show_employees()

# Демонстрация работы сотрудников
for employee in zoo.employees:
    employee.work()

# Демонстрация поведения животных
for animal in zoo.animals:
    animal.make_sound()
    animal.eat()
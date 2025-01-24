#ex 1

from abc import ABC, abstractmethod, ABCMeta
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def description(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def description(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def description(self):
        return f"Rectangle with width {self.width} and height {self.height}"

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("The given sides don't form a valid triangle.")
    def _is_valid_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
    def description(self):
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"

class ShapeManager:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("Object must be an instance of Shape.")
        self.shapes.append(shape)
    def calculate_all(self):
        for shape in self.shapes:
            print(shape.description())
            print(f"Area: {shape.area():.2f}")
            print(f"Perimeter: {shape.perimeter():.2f}")
            print("-" * 30)


manager = ShapeManager()

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

manager.add_shape(circle)
manager.add_shape(rectangle)
manager.add_shape(triangle)

manager.calculate_all()

#ex 2

class ValidationMeta(ABCMeta):
    def __new__(cls, name, bases, class_dict):
        methods = [key for key, value in class_dict.items() if callable(value)]
        invalid_methods = [method for method in methods if not method.startswith("do_")]
        if invalid_methods:
            raise ValueError(f"Клас має методи, які не починаються з 'do_'")
        if 'description' not in class_dict:
            class_dict['description'] = "Default description"
        elif not isinstance(class_dict['description'], str):
            raise ValueError(f"Атрибут 'description' у класі повинен бути рядком.")

        return super().__new__(cls, name, bases, class_dict)

class ValidatedClass(ABC, metaclass=ValidationMeta):
    pass

try:

    class ValidClass(ValidatedClass):
        description = "Правильний клас."

        def do_task(self):
            pass

        def do_something_else(self):
            pass

except Exception as e:
    print(f"Помилка при створенні класу: {e}")

try:

    class InvalidClass1(ValidatedClass):
        description = "Неправильний метод."

        def task(self):
            pass

except Exception as e:
    print(f"Помилка при створенні класу: {e}")

try:

    class InvalidClass2(ValidatedClass):
        def do_task(self):
            pass

except Exception as e:
    print(f"Помилка при створенні класу: {e}")

try:

    class InvalidClass3(ValidatedClass):
        description = 123

        def do_task(self):
            pass

except Exception as e:
    print(f"Помилка при створенні класу: {e}")
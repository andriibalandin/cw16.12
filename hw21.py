#ex 1
class Airplane:
    def __init__(self, model, passengers: int):
        if not isinstance(passengers, int):
            raise TypeError("Passengers must be an integer")
        self.passengers = passengers
        self.model = model
    @classmethod
    def passenger_verification(cls, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError("Second variable should be int or airplane")
        return other if isinstance(other, int) else other.passengers
    def __eq__(self, other):
        if not isinstance(other, (str, Airplane)):
            raise TypeError("Second variable should be str or airplane")
        temp = other if isinstance(other, str) else other.model
        return self.model == temp
    def __le__(self, other):
        temp = self.passenger_verification(other)
        return self.passengers <= temp
    def __ge__(self, other):
        temp = self.passenger_verification(other)
        return self.passengers >= temp
    def __lt__(self, other):
        temp = self.passenger_verification(other)
        return self.passengers < temp
    def __add__(self, other):
        temp = self.passenger_verification(other)
        return self.passengers + temp
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        temp = self.passenger_verification(other)
        self.passengers += temp
        return self
    def __sub__(self, other):
        temp = self.passenger_verification(other)
        return self.passengers - temp
    def __rsub__(self, other):
        return self - other
    def __isub__(self, other):
        temp = self.passenger_verification(other)
        self.passengers -= temp
        return self

Boeing = Airplane("Boeing 737-800", 189)
Airbus = Airplane("Airbus A320", 180)
Airbus2 = Airplane("Airbus A320", 180)

print(Boeing <= Airbus)
print(Airbus2 >= 210)
print(Boeing > Airbus)
print(124 + Airbus2)
Airbus2 += 444
print(Airbus2.passengers)
print(Boeing == Airbus)
print(Boeing == "Boeing 737-800")
print("Boeing 737-800" == Boeing)
print("========================")

#ex 2

class Flat:
    def __init__(self, area: float, price: float):
        if not isinstance(area, (int, float)) or not isinstance(price, (int, float)):
            raise TypeError("Area and price must be numbers")
        self.area = area
        self.price = price
    @classmethod
    def value_verification(cls, other, attr):
        if not isinstance(other, (int, float, Flat)):
            raise TypeError("Comparison must be with a number or a Flat object")
        return getattr(other, attr) if isinstance(other, Flat) else other
    def __eq__(self, other):
        temp = self.value_verification(other, 'area')
        return self.area == temp
    def __ne__(self, other):
        temp = self.value_verification(other, 'area')
        return self.area != temp
    def __lt__(self, other):
        temp = self.value_verification(other, 'price')
        return self.price < temp
    def __le__(self, other):
        temp = self.value_verification(other, 'price')
        return self.price <= temp
    def __gt__(self, other):
        temp = self.value_verification(other, 'price')
        return self.price > temp
    def __ge__(self, other):
        temp = self.value_verification(other, 'price')
        return self.price >= temp

Flat1 = Flat(20, 480000)
Flat2 = Flat(25, 840000)
print(Flat2 < 1000000)
print(Flat1 == Flat2)
print(20 == Flat1)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def save(self, filename):
        pass
    @staticmethod
    @abstractmethod
    def load(filename):
        pass

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    def show(self):
        print(f"Square: Top-left corner=({self.x}, {self.y}), Side length={self.side}")
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Square {self.x} {self.y} {self.side}\n")
    @staticmethod
    def load(filename):
        with open(filename, 'r') as file:
            data = file.readline().strip().split()
        return Square(int(data[1]), int(data[2]), int(data[3]))

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        print(f"Rectangle: Top-left corner=({self.x}, {self.y}), Width={self.width}, Height={self.height}")
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Rectangle {self.x} {self.y} {self.width} {self.height}\n")
    @staticmethod
    def load(filename):
        with open(filename, 'r') as file:
            data = file.readline().strip().split()
        return Rectangle(int(data[1]), int(data[2]), int(data[3]), int(data[4]))

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def show(self):
        print(f"Circle: Center=({self.x}, {self.y}), Radius={self.radius}")
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Circle {self.x} {self.y} {self.radius}\n")
    @staticmethod
    def load(filename):
        with open(filename, 'r') as file:
            data = file.readline().strip().split()
        return Circle(int(data[1]), int(data[2]), int(data[3]))

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        print(f"Ellipse: Bounding box top-left corner=({self.x}, {self.y}), Width={self.width}, Height={self.height}")
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(f"Ellipse {self.x} {self.y} {self.width} {self.height}\n")
    @staticmethod
    def load(filename):
        with open(filename, 'r') as file:
            data = file.readline().strip().split()
        return Ellipse(int(data[1]), int(data[2]), int(data[3]), int(data[4]))

shapes = [
    Square(0, 0, 10),
    Rectangle(1, 1, 20, 15),
    Circle(5, 5, 7),
    Ellipse(2, 2, 8, 4)
]

for i, shape in enumerate(shapes):
    shape.save(f"shape_{i}.txt")

loaded_shapes = []
for i in range(len(shapes)):
    with open(f"shape_{i}.txt", 'r') as file:
        shape_type = file.readline().split()[0]
        if shape_type == 'Square':
            loaded_shapes.append(Square.load(f"shape_{i}.txt"))
        elif shape_type == 'Rectangle':
            loaded_shapes.append(Rectangle.load(f"shape_{i}.txt"))
        elif shape_type == 'Circle':
            loaded_shapes.append(Circle.load(f"shape_{i}.txt"))
        elif shape_type == 'Ellipse':
            loaded_shapes.append(Ellipse.load(f"shape_{i}.txt"))

for shape in loaded_shapes:
    shape.show()

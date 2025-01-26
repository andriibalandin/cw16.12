# ex 1
from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.brand = None
        self.body_type = None
        self.color = None
        self.engine_type = None
        self.doors = None
        self.options = []

    def __str__(self):
        return (f"Car(brand={self.brand}, body_type={self.body_type}, color={self.color}, "
                f"engine_type={self.engine_type}, doors={self.doors}, options={self.options})")


class CarBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_body_type(self, body_type):
        self.car.body_type = body_type
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine_type(self, engine_type):
        self.car.engine_type = engine_type
        return self

    def set_doors(self, doors):
        self.car.doors = doors
        return self

    def add_option(self, option):
        self.car.options.append(option)
        return self

    def build(self):
        car = self.car
        self.reset()
        return car


class Director:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_electric_sedan(self):
        return (self.builder
                .set_brand("Tesla")
                .set_body_type("sedan")
                .set_color("red")
                .set_engine_type("electric")
                .set_doors(4)
                .add_option("autopilot")
                .add_option("panoramic roof")
                .build())

    def construct_suv(self):
        return (self.builder
                .set_brand("BMW")
                .set_body_type("SUV")
                .set_color("black")
                .set_engine_type("diesel")
                .set_doors(5)
                .add_option("leather interior")
                .add_option("all-wheel drive")
                .build())


builder = CarBuilder()
director = Director(builder)

electric_sedan = director.construct_electric_sedan()
suv = director.construct_suv()
print(electric_sedan)
print(suv)

# ex 2


class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_toppings(self):
        pass

    @abstractmethod
    def get_addons(self):
        pass

class Carbonara(Pasta):
    def get_type(self):
        return "Spaghetti"

    def get_sauce(self):
        return "Eggs and cheese sauce"

    def get_toppings(self):
        return "Bacon"

    def get_addons(self):
        return ["Black pepper", "Parmesan"]

class Bolognese(Pasta):
    def get_type(self):
        return "Fettuccine"

    def get_sauce(self):
        return "Tomato sauce"

    def get_toppings(self):
        return "Ground beef"

    def get_addons(self):
        return ["Basil", "Parmesan"]

class VegetarianPasta(Pasta):
    def get_type(self):
        return "Penne"

    def get_sauce(self):
        return "Tomato sauce"

    def get_toppings(self):
        return "Grilled vegetables"

    def get_addons(self):
        return ["Olive oil", "Oregano"]

class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "Carbonara":
            return Carbonara()
        elif pasta_type == "Bolognese":
            return Bolognese()
        elif pasta_type == "Vegetarian":
            return VegetarianPasta()
        else:
            raise ValueError(f"Unknown pasta type: {pasta_type}")



factory = PastaFactory()

carbonara = factory.create_pasta("Carbonara")
print(f"Type: {carbonara.get_type()}, Sauce: {carbonara.get_sauce()}, Toppings: {carbonara.get_toppings()}, Addons: {carbonara.get_addons()}")

bolognese = factory.create_pasta("Bolognese")
print(f"Type: {bolognese.get_type()}, Sauce: {bolognese.get_sauce()}, Toppings: {bolognese.get_toppings()}, Addons: {bolognese.get_addons()}")

vegetarian = factory.create_pasta("Vegetarian")
print(f"Type: {vegetarian.get_type()}, Sauce: {vegetarian.get_sauce()}, Toppings: {vegetarian.get_toppings()}, Addons: {vegetarian.get_addons()}")
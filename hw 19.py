# ex 1

class Passport:
    def __init__(self, first_name, last_name, date_of_birth, passport_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__passport_number = passport_number
    def show_info(self):
        return {
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "date_of_birth": self.__date_of_birth,
            "passport_number": self.__passport_number
        }

class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, date_of_birth, passport_number, foreign_passport_number):
        super().__init__(first_name, last_name, date_of_birth, passport_number)
        self.__foreign_passport_number = foreign_passport_number
        self.__visas = []
    def add_visa(self, country, issue_date, expiry_date):
        self.__visas.append({
            "country": country,
            "issue_date": issue_date,
            "expiry_date": expiry_date
        })
    def show_info(self):
        info = super().show_info()
        info["foreign_passport_number"] = self.__foreign_passport_number
        info["visas"] = self.__visas
        return info

pass1 = ForeignPassport("Andrii", "Balandin", "08-06-2004", "00000", "11111")
pass1.add_visa("Italy", "01-01-2025", "01-01-2027")
print(pass1.show_info())

# ex 2

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        return (f"Device Information:\nBrand: {self.brand}\nModel: {self.model}")

class CoffeeMachine(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    def make_coffee(self):
        return "Brewing coffee..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nWater Tank Capacity: {self.capacity}L"

class Blender(Device):
    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels
    def blend(self):
        return "Blending..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nSpeed Levels: {self.speed_levels}"

class MeatGrinder(Device):
    def __init__(self, brand, model, blade_material):
        super().__init__(brand, model)
        self.blade_material = blade_material
    def grind_meat(self):
        return "Grinding..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nBlade Material: {self.blade_material}"

coffeemachine = CoffeeMachine("Philips", "EP3347", 1.8)
print(coffeemachine.show_info())
print(coffeemachine.make_coffee())
print("")
blender = Blender("Tefal", "HB6568", 20)
print(blender.show_info())
print(blender.blend())
print("")
meatgrinder = MeatGrinder("Bosch", "MFW68660", "Stainless Steel")
print(meatgrinder.show_info())
print(meatgrinder.grind_meat())

# ex 3

class Ship:
    def __init__(self, name, country, displacement):
        self.name = name
        self.country = country
        self.displacement = displacement
    def show_info(self):
        return (f"Ship Information:\n"
                f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Displacement: {self.displacement} tons")

class Frigate(Ship):
    def __init__(self, name, country, displacement, weapon_system):
        super().__init__(name, country, displacement)
        self.weapon_system = weapon_system
    def deploy_weapons(self):
        return "Frigate deploying weapon systems..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nWeapon System: {self.weapon_system}"

class Destroyer(Ship):
    def __init__(self, name, country, displacement, radar_system):
        super().__init__(name, country, displacement)
        self.radar_system = radar_system
    def engage_enemy(self):
        return "Destroyer engaging enemy targets..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nRadar System: {self.radar_system}"

class Cruiser(Ship):
    def __init__(self, name, country, displacement, armor_thickness):
        super().__init__(name, country, displacement)
        self.armor_thickness = armor_thickness
    def lead_fleet(self):
        return "Cruiser leading the fleet..."
    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}\nArmor Thickness: {self.armor_thickness} cm"

frigate = Frigate("HMS Iron Duke", "UK", 4200, "Sea Ceptor")
print(frigate.show_info())
print(frigate.deploy_weapons())
print("")
destroyer = Destroyer("USS Arleigh Burke", "USA", 9000, "AN/SPY-1D")
print(destroyer.show_info())
print(destroyer.engage_enemy())
print("")
cruiser = Cruiser("HMCS Halifax", "Canada", 11300, 20)
print(cruiser.show_info())
print(cruiser.lead_fleet())

# ex 4

class Money:
    def __init__(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part
    def show(self):
        return f"{self.whole_part}.{self.fractional_part}"
    def set_money(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

class Product(Money):
    def __init__(self, whole_part, fractional_part, name):
        super().__init__(whole_part, fractional_part)
        self.name = name
    def reduce_price(self, reduction_whole, reduction_fractional):
        total_cents = (self.whole_part * 100 + self.fractional_part) - (reduction_whole * 100 + reduction_fractional)
        self.whole_part = total_cents // 100
        self.fractional_part = total_cents % 100
    def show_product(self):
        return f"Product: {self.name}, Price: {self.show()}"

money = Money(10, 550)
print("Money:", money.show())
money.set_money(15, 75)
print("Updated Money:", money.show())
print("")
product = Product(100, 99, "Laptop")
print(product.show_product())
product.reduce_price(10, 50)
print("After Reduction:", product.show_product())

# ex 5

class TemperatureConverter:
    conversion_count = 0
    @staticmethod
    def c_to_f(celsius):
        TemperatureConverter.conversion_count += 1
        return celsius * 9 / 5 + 32
    @staticmethod
    def f_to_c(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5 / 9
    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

print("0°C to Fahrenheit:", TemperatureConverter.c_to_ft(0))
print("32°F to Celsius:", TemperatureConverter.f_to_c(32))
print("Conversions performed:", TemperatureConverter.get_conversion_count())

# ex 6

class MetricToImperialConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084
    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371
    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371

print("10 meters to feet:", MetricToImperialConverter.meters_to_feet(10))
print("32.8 feet to meters:", MetricToImperialConverter.feet_to_meters(32.8))
print("5 kilometers to miles:", MetricToImperialConverter.kilometers_to_miles(5))
print("3.1 miles to kilometers:", MetricToImperialConverter.miles_to_kilometers(3.1))

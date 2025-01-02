# ex 1
import datetime

class Human:
    def __init__(self, name, birthdate, phonenum, city, country, address):
        self.name = name
        self.birthdate = birthdate
        self.phonenum = phonenum
        self.city = city
        self.country = country
        self.address = address
    def showinfo(self):
        print(f"Name: {self.name}\nBirthdate: {self.birthdate}\nPhone number: {self.phonenum}\nCity: {self.city}\nCountry: {self.country}\nAddress: {self.address}")
    def is_major(self):
        birthdate = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d")
        today = datetime.datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age >= 18

hum1 = Human("Balandin Andrii", "2004-06-08", "0688888888", "Dnipro", "Ua", "Zach 4")
print(hum1.is_major())

# ex 2

class City:
    def __init__(self, name, region, country, population, zipcode, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipcode = zipcode
        self.phone_code = phone_code
    def showinfo(self):
        print(f"City: {self.name}\nRegion: {self.region}\nCounty: {self.country}\nPopulation: {self.population}\nZipcode: {self.zipcode}\nPhone code: {self.phone_code}")
    def is_valid_zipcode(self):
        return self.zipcode.isdigit() and len(self.zipcode) == 5

city = City("Дніпро", "Дніпропетровська область", "Україна", 968250, "49000", "056")
city.showinfo()
print(city.is_valid_zipcode())

# ex 3-5

class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities
    def display_data(self):
        print(f"Country: {self.name}\nContinent: {self.continent}\nPopulation: {self.population}\nPhone code: {self.phone_code}\nCapital: {self.capital}\nCities: {', '.join(self.cities)}")

class Car:
    def __init__(self, model, year, manufacturer, enginevolume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.enginevolume = enginevolume
        self.color = color
        self.price = price
    def showinfo(self):
        print(f"Model: {self.model}\nYear: {self.year}\nManufacturer: {self.manufacturer}\nEngine Volume: {self.enginevolume}\nColor: {self.color}\nPrice: {self.price}")

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    def display_data(self):
        print(f"Title: {self.title}\nYear: {self.year}\nPublisher: {self.publisher}\nGenre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price}")
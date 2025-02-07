import json
import pickle
import os
# ex1


class CapitalsManager:
    def __init__(self):
        self.data = {}

    def add(self, country, capital):
        self.data[country] = capital

    def remove(self, country):
        if country in self.data:
            del self.data[country]

    def search(self, country):
        return self.data.get(country, "This country not in the list")

    def edit(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file)

    def load(self, filename):
        with open(filename, "r") as file:
            self.data = json.load(file)


def ex1check():
    manager = CapitalsManager()
    manager.add("Ukraine", "Kyiv")
    manager.add("France", "Paris")
    print(manager.search("Ukraine"))
    manager.edit("Ukraine", "Kyiv2")
    manager.save("countries.json")
    manager.load("countries.json")
    print(manager.search("Ukraine"))

#ex1check()

# ex2


class Pickle_Manager:
    @staticmethod
    def save(filename, obj):
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def load(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)


class Json_Manager:
    @staticmethod
    def save(filename, obj):
        with open(filename, "w") as file:
            json.dump(obj.convert_to_dict(), file, indent=4)

    @staticmethod
    def load(filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return Airplane.convert_from_dict(data)


class Airplane:
    def __init__(self, model, number):
        self.model = model
        self.number = number

    def change_model(self, new_model):
        self.model = new_model

    def change_number(self, new_number):
        self.number = new_number

    def fly_to(self, point):
        print(f"Plane {self.model}({self.number}) flew to the {point}")

    def convert_to_dict(self):
        return {
            'model': self.model,
            'number': self.number
        }

    @classmethod
    def convert_from_dict(cls, data):
        return cls(
            model=data['model'],
            number=data['number']
        )


def ex2check():
    plane1 = Airplane("Boing", "G4521")
    Json_Manager.save("../plane1.json", plane1)
    print(Json_Manager.load("../plane1.json"))
    plane2 = Airplane("Airbus", "H9421")
    Pickle_Manager.save("../plane2.pkl", plane2)
    print(Pickle_Manager.load("../plane2.pkl"))

#ex2check()
# ex3


class User:
    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    def conv_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

    @classmethod
    def conv_from_dict(cls, user):
        return cls(
            user["id"],
            user["name"],
            user["age"],
            user["email"]
        )

class Users_Manager:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                try:
                    return json.load(file)
                except Exception:
                    return []
        return []

    def read_users(self):
        return self.users

    def read_user(self, id):
        return self.users[id - 1]

    def add_user(self, user):
        return self.users.append(user.conv_to_dict())

    def update_age(self, id, new_age):
        self.users[id - 1]["age"] = new_age

    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file, indent=4)


def ex3check():
    manager = Users_Manager("users.json")
    print(type(manager.users))
    print(manager.read_users)
    manager.update_age(2, 30)
    new_user = User(4, "Emma", 28, "emma@example.com")
    manager.add_user(new_user)
    print(manager.read_users())
    manager.save_users()


#ex3check()

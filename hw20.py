#ex 1
class Film:
    films = []
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        Film.films.append(self)
    @classmethod
    def avg_rate(cls):
        if not cls.films:
            return 0
        total_rating = sum(film.rating for film in cls.films)
        return total_rating / len(cls.films)
    @classmethod
    def show_rate(cls):
        for film in cls.films:
            print(f"Фільм: {film.name}, Рейтинг: {film.rating}")
    @classmethod
    def show_names(cls):
        for film in cls.films:
            print(f"Фільм: {film.name}")

film1 = Film("Lock, Stock and Two Smoking Barrels", 8.6)
film2 = Film("Snatch", 8.6)
film3 = Film("The Gentleman", 7.8)
print("Рейтинги всіх фільмів:")
Film.show_rate()
print("\nНазви всіх фільмів:")
Film.show_names()
avg = Film.avg_rate()
print(f"\nСередній рейтинг всіх фільмів: {avg:.2f}")

#ex 2

class Brain:
    def think(self):
        print("thinking...")
class Heart:
    def beat(self):
        print("beating")
class Legs:
    def walk(self):
        print("walking...")
class Eyes:
    def look(self):
        print("looking...")
class Mouth:
    def speak(self):
        print("speaking...")
class Human(Brain, Heart, Legs, Eyes, Mouth):
    def live(self):
        print("Human is alive")

Human.live()
Human.look()
Human.speak()
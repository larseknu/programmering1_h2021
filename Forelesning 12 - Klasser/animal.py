class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def print_information(self):
        print(f"{self.name} is a {self.species}")

honeybadger = Animal("Nils", "Honeybadger", 8)
print(print(f"{honeybadger.name} is a {honeybadger.species}"))
honeybadger.name = "John"
honeybadger.print_information()
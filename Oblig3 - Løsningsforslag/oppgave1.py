animal = {
    "species": "Honey Badger",
    "name": "Nils",
    "sex": "Male"
}

# A
print(animal['name'])
# B
animal['sex'] = "Female"
print(animal)
# C
animal['age'] = 8
print(f"\n{animal['name']} er {animal['age']} år")

print(animal)


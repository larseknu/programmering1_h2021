cities = {
    "fredrikstad": {"country": "Norway", "population": 78000, "fact": "Norway's nicest city!"},
    "tokyo": {"country": "Japan", "population": 37339000, "fact": "Sushi capital!"},
}
print(cities)

# Addina  new city
cities["seoul"] = {"country": "South Korea", "population": 9968000, "fact": "38m above sea level and has k-pop"}

print(cities)

# Iterates through all cities and prints info about them
for city, city_info in cities.items():
    country = city_info['country']
    #population = city_info['population']

    print(f"\n{city.title()} is in {country}")
    print(f"\tIt has a population of {city_info['population']}")
    print(f"\tAn interesting fact about {city.title()}: {city_info['fact']}")


# Print all the info about Seoul in a dictionary format
print(f"\nInfo about Seoul: {cities['seoul']}")

# Prints the population of Seoul
print(f"\nSeoul has a population of: {cities['seoul']['population']} people")

# Gets a reference to the information about Seoul
seoul_info = cities['seoul']
# Prints the population of Seoul
print(f"\nSeoul has a population of: {seoul_info['population']} people")
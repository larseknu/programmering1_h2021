def print_cities_information(cities):
    # Iterates through all cities and prints info about them
    for city, city_info in cities.items():
        country = city_info['country']
        #population = city_info['population']

        print(f"\n{city.title()} is in {country}")
        print(f"\tIt has a population of {city_info['population']}")
        print(f"\tAn interesting fact about {city.title()}: {city_info['fact']}")

        #print(f"Is capitol: {city_info.get('is_capitol', False)}")
        if city_info.get('is_capitol', False):
            print("\tIs the capitol!")


def increase_population(cities, percent=1.05):
    for city_info in cities.values():
        city_info['population'] *= percent


def set_if_capital_or_not(cities, city_name, is_capitol=False):
    cities[city_name]['is_capitol'] = is_capitol


cities = {
    "fredrikstad": {"country": "Norway", "population": 78000, "fact": "Norway's nicest city!"},
    "tokyo": {"country": "Japan", "population": 37339000, "fact": "Sushi capital!"},
    "seoul": {"country": "South Korea", "population": 9968000, "fact": "38m above sea level and has k-pop"}
}


print_cities_information(cities)
increase_population(cities, 1.10)
print_cities_information(cities)

set_if_capital_or_not(cities, 'fredrikstad', False)
set_if_capital_or_not(cities, 'tokyo', True)
set_if_capital_or_not(cities, 'seoul', True)

print_cities_information(cities)

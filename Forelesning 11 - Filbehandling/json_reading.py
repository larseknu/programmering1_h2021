import json

planets = [{'name': 'Random'},
           {'name': 'Mercury', 'gravity': 3.7},
           {'name': 'Venus', 'gravity': 8.87},
           {'name': 'Earth', 'gravity': 9.807},
           {'name': 'Mars', 'gravity': 3.721},
           {'name': 'Jupiter', 'gravity': 24.79},
           {'name': 'Saturn', 'gravity': 10.44},
           {'name': 'Uranus', 'gravity': 8.87},
           {'name': 'Neptune', 'gravity': 11.15}]

with open("planets.json", "w") as output_file:
    json.dump(planets, output_file, indent=4)

with open("planets.json", "r") as output_file:
    planets_from_file = json.load(output_file)

    print(planets_from_file)






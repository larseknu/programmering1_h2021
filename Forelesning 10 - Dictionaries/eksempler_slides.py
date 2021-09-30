movie = {'title': 'Soul', 'year': 2020, 'duration': 100, 'score': 8.4}

print(movie['title'])
print(f"{movie.get('duration')} min")


movie['director'] = 'Pete Docter'

print(movie)
movie = {'title': 'Soul', 'year': 2020, 'duration': 100, 'score': 8.4, 'director': 'Pete Docter'}

movie.pop('director')
print(movie)

del movie['score']
print(movie)

print(movie.get('score'))

movie = {'title': 'Soul', 'year': 2020, 'duration': 100, 'score': 8.4}

for key in movie:  # Kan også bruke movie.keys()
    print(f"{key}")

for value in movie.values():
    print(f"{value}")

for key, value in movie.items():
    print(f"{key} - {value}")

x, y = 5, 6

for key, value in sorted(movie.items()):
    print(f"{key} - {value}")

movies = [
    {'title': 'Soul', 'year': 2020, 'duration': 100},
    {'title': 'Dune', 'year': 2021, 'duration': 156},
]

print("\nMovies loop from list:")
for movie in movies:
    print(f"{movie['title']} was released in {movie['year']}")

movies.append({'title': 'Joker', 'year': 2019, 'duration': 121})

print("\nMovies loop from list after append:")
for movie in movies:
    print(f"{movie['title']} was released in {movie['year']}")

# Skrive ut informasjon om én film
soul = movies[0]
print(f"\nOne movie from list:\n{soul['title']} was released in {soul['year']}")

movies = {
    'soul2020': {'title': 'Soul', 'year': 2020, 'duration': 100},
    'dune2021': {'title': 'Dune', 'year': 2021, 'duration': 156},
    'joker2019': {'title': 'Joker', 'year': 2019, 'duration': 121},
}

print("\nMovies loop from dictionary:")
for key, movie in movies.items():
    print(f"{key} - {movie[key]} was released in {movie['year']}")

# Skrive ut informasjon om én film
dune = movies['dune2021']
print(f"\nOne movie from list:\n{dune['title']} was released in {dune['year']}")
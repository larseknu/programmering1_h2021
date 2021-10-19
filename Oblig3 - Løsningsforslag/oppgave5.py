from oppgave5_moviefunctions import *

movies = [{'name': 'Inception', 'year': 2010, 'rating': 8.7},
          {'name': 'Inside Out', 'year': 2015, 'rating': 8.1},
          {'name': 'Con Air', 'year': 1997, 'rating': 6.9}]

bad_movies = []

add_movie(bad_movies, 'The Hulk', 1984,  4.5)
add_movie(bad_movies, 'I kill you 3', 1996, 3.4)

add_movie(movies, 'Finch', 2021, 8.30)
add_movie(movies, 'Luca', 2020)
add_movie(movies, 'No Time to Die', 2021, 9.1)
add_movie(movies, 'Giant', 1965, 7.6)

print_movies(movies)
print("\nBAD movies:")
print_movies(bad_movies)

print(f"\nThe average rating of movies is: {average_movie_rating(movies)}")
print(f"\nThe average rating of BAD movies is: {average_movie_rating(bad_movies)}")

movies_after_2010 = get_movies_after_year(movies, 2010)
print(f"\nThe average rating of 2010 movies is: {average_movie_rating(movies_after_2010)}\n")
print_movies(movies_after_2010)

write_movie_title_to_file(movies, "my_movies.txt")
write_movie_title_to_file(bad_movies, "bad_movies.txt")

print("\nFROM BAD MOVIES FILE:")
read_and_print_file("bad_movies.txt")

print("\nFROM MY MOVIES FILE:")
read_and_print_file("my_movies.txt")

print("\nOppgave1:")
read_and_print_file("oppgave1.py")


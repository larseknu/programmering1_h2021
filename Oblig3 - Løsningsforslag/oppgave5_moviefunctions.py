def add_movie(movies_list, name, year, rating=5.0):
    movies_list.append({'name': name, 'year': year, 'rating': rating})


def print_movies(movies_list):
    for movie in movies_list:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")


def average_movie_rating(movie_list):
    sum_ratings = 0.0
    for movie in movie_list:
        sum_ratings += movie['rating']

    return sum_ratings / len(movie_list)


def get_movies_after_year(movie_list, year):
    movies_after_year = []
    for movie in movie_list:
        if movie['year'] >= year:
            movies_after_year.append(movie)

    return movies_after_year


def write_movie_title_to_file(movie_list, filename):
    with open(filename, 'w') as movie_file:
        for movie in movie_list:
            movie_file.write(f"{movie['name']}\n")


def read_and_print_file(filename):
    file = open(filename, 'r')
    print(file.read())
    file.close()

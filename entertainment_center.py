import csv
import media
import fresh_tomatoes

def create_movies(file_name):
    """
    Reads from a CSV file containing four columns:
    Movie title, movie description, movie poster url, and movie trailer url

    Returns a list of Movie objects
    """
    movies = list()
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()  # Get the header row

        for movie in reader:
            movies.append(media.Movie(movie[0], movie[1], movie[2], movie[3]))

    return movies


def create_movie_page(movies):
    """
    Takes in a list of Movie objects and creates a web page using fresh_tomatoes
    """
    fresh_tomatoes.open_movies_page(movies)


if __name__=="__main__":
    create_movie_page(create_movies('movies.csv'))

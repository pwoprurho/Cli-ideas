from imdb import IMDb

def get_movie_rating():
    movie_name = input("Enter the name of the movie: ")
    lala = IMDb()
    movies = lala.search_movie(movie_name)
    if movies:
        movie = movies[0]
        lala.update(movie)
        rating = movie.get("rating", "N/A")
        print(f"The IMDB rating of {movie_name} is: {rating}")
    else:
        print(f"The movie titled ({movie_name}) is not found")
get_movie_rating()
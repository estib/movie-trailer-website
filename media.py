__author__ = 'Steve'

# This file will create a class "movie" that will contain all the data/attributes that the "fresh tomatoes" site will
# display to the user. Which data/movie attributes are included should be pretty self-explanatory.


class Movie():

    def __init__(self, movie_title, movie_storyline, movie_poster_img, movie_youtube, movie_imdb):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_img
        self.trailer_youtube_url = movie_youtube
        self.imdb_url = movie_imdb  # imdb = "Internet Movie Database", a popular movie critic site.
        self.fandango = "http://www.fandango.com/search/?q=" + movie_title.lower().replace(" ", "%20")
        # Fandango: In case users want to try to buy tickets to the movie.
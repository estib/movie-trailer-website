__author__ = 'Steve'

# Running this program will prompt a new page in a browser to show a series of
# movie titles, poster images, and movie trailers for 6 pretty good movies that
# came out fairly recently. It will also include links to each movie's profile
# in IMDb ("Internet Movie Database") and to where the user can buy tickets for
# each movie on Fandango.com, if tickets are available.


import media
import fresh_tomatoes


# Instantiate 6 movies that will be shown to the user on the "fresh tomatoes"
# site. Each object takes the following attributes:
#   1. The Movie Title
#   2. A brief description of the movie
#   3. A link to the poster-image of the movie
#   4. A link to the movie trailer on youtube.com
#   5. A link to the movie's IMDb profile

Budapest_Hotel = media.Movie(
    "The Grand Budapest Hotel",
    "The comical story of how Zero comes to acquire a specially valuable \
    hotel and its rare 'Boy with Apple' painting.",
    "http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
    "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
    "http://www.imdb.com/title/tt2278388/")

Calvary = media.Movie(
    "Calvary",
    "How Fr. James spends what might be his last 7 days alive after a man in \
    his congregation confesses his plans to kill him.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcT3Q6xAsCExaU2kID2qI5z5cIjteMgQD3oZyofdplCsPfcfkwi1",
    "https://www.youtube.com/watch?v=LGM5rq_vX4U",
    "http://www.imdb.com/title/tt2234003/")

Birdman = media.Movie(
    "Birdman: Or (The Unexpected Virtue of Ignorance)",
    "Riggan Thomson, once famous for playing the role of 'Birdman' in an old \
    holywood blockbuster, now desperately tries to create real art by \
    writing, directing, and acting some Raymond Carver on Broadway.",
    "http://upload.wikimedia.org/wikipedia/en/thumb/a/a3/Birdman_poster.jpg/220px-Birdman_poster.jpg",
    "https://www.youtube.com/watch?v=uJfLoE6hanc",
    "http://www.imdb.com/title/tt2562232/")

Shawshank_Redemption = media.Movie(
    "The Shawshank Redemption",
    "Andy Dufresne is falsely condemned to prison for the murder of his wife. \
    He tries for a long, long time to escape.",
    "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=6hB3S9bIaco",
    "http://www.imdb.com/title/tt0111161/")

Populaire = media.Movie(
    "Populaire",
    "Rose Pamphyle tries to find a job as a secretary, but instead becomes \
    the world-champion at speed-typing on those old mechanical typewriters.",
    "http://ia.media-imdb.com/images/M/MV5BMjA2NzY4MDExOV5BMl5BanBnXkFtZTcwNTE4NzQzOQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=i6upoz9I7eg",
    "http://www.imdb.com/title/tt2070776/")

The_Double = media.Movie(
    "The Double",
    "Some dull office worker goes through a really trippy existential crisis \
    when his doppelganger shows up one day and challenges his own existence. \
    Based on the novella by Fyodor Dostoevsky.",
    "http://ia.media-imdb.com/images/M/MV5BMTExMzY5MjAwODZeQTJeQWpwZ15BbWU4MDg0NTcxNDAx._V1_SY317_CR4,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=XG8qATRtNuU",
    "http://www.imdb.com/title/tt1825157/")

movieList = [
    Budapest_Hotel, Calvary, Birdman, Shawshank_Redemption, Populaire,
    The_Double]

fresh_tomatoes.open_movies_page(movieList)

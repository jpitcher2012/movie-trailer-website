"""Create a list of movies and open a web page to display them."""

import fresh_tomatoes
import media


# Create the movie instances

toy_story = media.Movie(
    "Toy Story",
    "https://images-na.ssl-images-amazon.com/images/I/51RC8ZR6KBL.jpg",
    "https://www.youtube.com/watch?v=RmFbmlwWa0k")

finding_nemo = media.Movie(
    "Finding Nemo",
    "https://images-na.ssl-images-amazon.com/images/I/51XNP3ARK3L.jpg",
    "https://www.youtube.com/watch?v=KFu_26DrLE4")

inside_out = media.Movie(
    "Inside Out",
    "https://images-na.ssl-images-amazon.com/images/I/51g%2B1-GJCuL.jpg",
    "https://www.youtube.com/watch?v=y2truxhcBko")

wreck_it_ralph = media.Movie(
    "Wreck It Ralph",
    "https://images-na.ssl-images-amazon.com/images/I/61m64J4evuL._SY717_.jpg",
    "https://www.youtube.com/watch?v=OzMJkRwOxjs")

big_hero_6 = media.Movie(
    "Big Hero 6",
    "https://images-na.ssl-images-amazon.com/images/I/510nVoCaWtL.jpg",
    "https://www.youtube.com/watch?v=ihCciBFdbkw")

zootopia = media.Movie(
    "Zootopia",
    "https://images-na.ssl-images-amazon.com/images/I/71-Fj-WsM7L._SY717_.jpg",
    "https://www.youtube.com/watch?v=JOIjmLw0iQc")


# Add the movies to a list
movie_list = [toy_story, finding_nemo, inside_out,
              wreck_it_ralph, big_hero_6, zootopia]

# Open the web page with the list of movies
fresh_tomatoes.open_movies_page(movie_list)

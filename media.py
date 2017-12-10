"""Module defining the Movie class."""

import webbrowser


class Movie():
    """Class representing a movie object."""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Create a new movie instance.

        Arguments:
        title - movie's title
        poster_image_url - link to image that will be shown for movie
        trailer_youtube_url - link to movie's trailer in Youtube

        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

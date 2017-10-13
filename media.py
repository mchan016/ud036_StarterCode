class Movie():
    """Movie class containing relevant information to a Movie"""

    def __init__(self, title, description, poster_url, trailer_url):
        self.title = title
        self.description = description
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

import webbrowser


class Movie():
    # Initialize the movie class with multiple fields
    def __init__(self, title, year, description, rating, poster, trailer):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
    

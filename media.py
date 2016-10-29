from video import Video

class Movie(Video):
	"""Class media.py for category implementation"""
    def __init__(self, title, duration, category, trailer_youtube, poster_image_url, movie_storyline):
        Video.__init__(self, title, duration, category, trailer_youtube, poster_image_url)
        self.movie_storyline = movie_storyline
 

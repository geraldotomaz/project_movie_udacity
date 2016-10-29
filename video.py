class Video():
	"""Is class Father for media.py and TvShow.py"""
    def __init__(self, title, duration, category, trailer_youtube_url, poster_image_url):
        print("Instance class video")
        self.title = title
        self.duration = duration
        self.category = category
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        


from video import Video

class TvShow(Video):
	"""Class TvShow.py for category implementation"""
    def __init__(self, title, duration, category, trailer_youtube_url, poster_image_url, season, episode, tv_station):
        Video.__init__(self, title, duration, category, trailer_youtube_url, poster_image_url)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
          



        

        

import urllib
import json

class Movie():
    """ This class provides a way to store movie related information. It uses omdb api(open source movie database) to
    collect information about movies and the youtube data api to collect the movie trailers"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, name):
        movie = urllib.urlopen("http://www.omdbapi.com/?t=" + name + "&y=&plot=short&r=json")
        movie = json.load(movie)
        movie_trailer = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + name +"%20trailer&key=AIzaSyBDQ5R6qTn8sOCzBYiHsmUVaHlAU6Sq0K0")
        movie_trailer = json.load(movie_trailer)
        self.title = str(movie["Title"])
        self.storyline = str(movie["Plot"])
        self.poster_image_url = str(movie["Poster"])
        self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + movie_trailer["items"][0]["id"]["videoId"]

    def print_information(self):
        print(self.title)
        print(self.storyline)

    def test(self):
        movie_trailer = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=casino%20trailer&key=AIzaSyBDQ5R6qTn8sOCzBYiHsmUVaHlAU6Sq0K0")
        movie_trailer = json.load(movie_trailer)
        print(movie_trailer["items"][0]["id"]["videoId"])



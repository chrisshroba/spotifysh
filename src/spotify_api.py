__author__ = 'chrisshroba'
from operator import itemgetter
from time import sleep

import urllib.request
import urllib.parse
import json
from spotify_desktop import *


class Track(object):
    name = None
    artists = None
    song_hash = None
    popularity = None
    def __init__(self, name, artists, song_hash, popularity):
        self.name = name
        self.artists = artists
        self.song_hash = song_hash
        self.popularity = popularity

    def __str__(self):
        return "<Track \"{}\">".format(self.name)
class SpotifyClient(object):
    base_url = "https://api.spotify.com"
    def __init__(self):
        pass
    def request(self, url):
        full_url = self.base_url + url
        return json.loads(urllib.request.urlopen(full_url).read().decode("utf-8"))

    def search(self, query, limit=20, types_list=list(["track"])):
        types = ",".join(types_list)
        query = urllib.parse.quote(query)
        url = "/v1/search?q={query}&limit={limit}&type={types}".format_map(vars())
        response = self.request(url)
        try:
            tracks = [Track(
                name=item.get("name", ""),
                artists=map(itemgetter("name"), item.get("artists",[])),
                popularity=item.get("popularity"),
                song_hash=item.get("uri")
            ) for item in response["tracks"].get("items", [])]
            return tracks
        except Exception as e:
            return []

cl = SpotifyClient()

while True:
    query = input("> ")
    track = cl.search(query, limit=1)[0]
    play_song_hash(track.song_hash)
# for result in results["tracks"]["items"]:
#     artists = map(itemgetter("name"), result["artists"])
#     track_name = result["name"]
#     pop = result["popularity"]
#     song_hash = result["uri"]
#     from src.spotify_desktop import *
#     play_song_hash(song_hash)
#     sleep(3)
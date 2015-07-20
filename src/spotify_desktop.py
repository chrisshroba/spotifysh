__author__ = 'chrisshroba'

import os


def tell_spotify(suffix):
    cmd = 'tell application "Spotify" to {}'.format(suffix)
    full_cmd="osascript -e \'{}\'".format(cmd)
    os.system(full_cmd)


def play():
    tell_spotify("play")


def pause():
    tell_spotify("pause")


def play_song_hash(song_hash):
    if song_hash.startswith("spotify:track:"):
        tell_spotify("play track \"{}\"".format(song_hash))
    else:
        tell_spotify("play track \"spotify:track:{}\"".format(song_hash))

# play_song_hash("4fTHdMTq0Znl3djLI1Typn")


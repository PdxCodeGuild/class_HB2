import pylyrics3
# https://github.com/jameswenzel/pylyrics3


bon_iver_lyrics = pylyrics3.get_artist_lyrics('bon iver')

print(bon_iver_lyrics)


while True:
    artist = input('What artist do you want to look up?')
    print(pylyrics3.get_artist_lyrics(artist))
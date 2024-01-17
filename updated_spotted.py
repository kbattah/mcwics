import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

scope = 'user-top-read playlist-read-private'

#replace with your Spotify infos
client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'
redirect_uri = 'YOUR_SPOTIFY_REDIRECT_URI'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))
top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')['items']

#STEP 1: analyse music
artists = {}
years = []
valences = []

for track in top_tracks:
    artist_name = track['artists'][0]['name']
    release_year = track['album']['release_date'][:4]

    artists[artist_name] = artists.get(artist_name, 0) + 1
    years.append(int(release_year))

    features = sp.audio_features(track['id'])[0]
    valences.append(features['valence'])


top_artist = max(artists, key=artists.get)

average_year = sum(years) / len(years)
average_valence = sum(valences) / len(valences)

# roasts
artist_roast = f"Can't believe you've listened to {top_artist} so much. Are they the only artist you know?"
era_roast = f"Your music taste is stuck in {int(average_year)}, huh? Time to explore some new tunes!"
mood_roast = "Always happy and upbeat, aren't you?" if average_valence > 0.5 else "Why so gloomy? Try some happier music!"

# print roasts
print(artist_roast)
print(era_roast)
print(mood_roast)

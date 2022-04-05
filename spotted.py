
import statistics
import spotipy
import matplotlib.pyplot as plt
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id="e28e187c50da4e9fabf3fb0a33f4ca7e", client_secret="6d94d0b1ecc644338e0815df3e877402")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

play=input("Paste your playlist's URL here:\n")

playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DWYzKmy0vGGcY"
playlist_URI = play.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

pop=[]
index=[]
dates=[]
valences=[]
dance=[]
i=1;

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]
    
    #Album for date
    album = track["track"]["album"]["name"]
    track_date = track["track"]["album"]["release_date"]
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    
    #Valence
    features=sp.audio_features(track_uri)[0]
    track_valence = features['valence']
    track_danceability = features['danceability']
    
    #if (track_pop!=0):
    
    dates.append(int(track_date[0:4]))
    pop.append(track_pop)
    valences.append(track_valence)
    dance.append(track_danceability)
    index.append(i)
    i+=1

insult="You're "

for feature in [dates, pop, valences, dance]:
    
    x=np.array(index)
    y=np.array(feature)

    avg = statistics.mean(feature)

    plt.scatter(x, y)
    plt.plot([1,i], [avg, avg], label="the average you")
    
    if feature==dates:
        norm=2000
        plt.title("RELEASE DATES OF YOUR SONGS")
        alabel="pretentious boomer                           literally a kid"
        if avg<2000:
            insult+="pretentious boomer, "
        else:
            insult+="uncultivated mf, "
        
    elif feature==pop:
        norm=50
        plt.title("POPULARITY OF YOUR SONGS")
        alabel="\"i bet you can even name one of their songs\"                                 only listens to spotify's top 50"
        if avg<=50:
            insult+="\"i bet you can even name one of their songs\" headass, "
        else:
            insult+=", only listens to spotify's top 50, "
            
    elif feature==valences:
        norm=0.5
        plt.title("MOOD OF YOUR SONGS")
        alabel="we get it you're sad                          wow! looks like therapy helps!"
        if avg<=0.5:
            insult+=", thinks their personality is listening to sad shit, "
        else:
            insult+=", who sometimes listens to happy shit! congrats, looks like the therapy helped!,  "
            
    else:
        norm=0.5
        plt.title("DANCEABILITY OF YOUR SONGS")
        alabel="wow you must be fun at parties                              no one wants to give you the aux cord at parties, stop it"
        if avg<=0.5:
            insult+="with 0 moves."
        else:
            insult+="aux-cord dictator."
    
    plt.xlabel("Track number")
    plt.ylabel(alabel)
    plt.plot([1,i], [norm, norm], 'r', label='the Norm')
    plt.legend(loc="upper right")
    plt.show()

print('\n'+insult)

    

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from itertools import islice

# The console version of Kinify.
# Setting up credentials
cid = 'CID'
secret = 'SECRET'
client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Initialize storage for the data that is required
track_id = {}
playlist_id = []

# Begin the search
print("Welcome to Kinify!")
character = input("Enter a character's name (e.g. Nagito Komaeda): ")

playlists = sp.search(q=character, limit = 50, type='playlist')
for i, playlist in enumerate(playlists['playlists']['items']):
    playlist_id.append(playlist['id'])

# Obtain the tracks in each playlist
for id in playlist_id:
    tracks = sp.playlist_items(id, fields='items.track.id', limit = 50)
    # Update the dictionary with the tracks in the playlist
    for track in enumerate(tracks['items']):
        # Check if the track already exists in the dictionary
        if track[1]['track'] == None:
            pass
        else:
            found = False
            for key in track_id:
                if key == track[1]['track']['id']:
                    track_id[key] += 1
                    found = True
                    break
            # Add track to dictionary if it's not there
            if found == False:
                track_id[track[1]['track']['id']] = 1

# Sort based on frequency
sorted_tracks = sorted(track_id, key = track_id.get, reverse = True)
# Obtain the top 10 tracks and print results
top_ten_ids = islice(sorted_tracks, 10)
print("Fans of " + character + " really like...")
for t in top_ten_ids:
    if t is None:
        pass
    else: 
        song = sp.track(t)
        print("- " + song['name'] + " by " + song['artists'][0]['name'])

import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        redirect_uri=os.getenv("MY_URI"),
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Get Playlist Track Date and Song ID Together as Dict
def get_playlist(playlist_id):
    all_release_date = {}
    offset = 0
    while True:
        track_data = sp.playlist_tracks(playlist_id=playlist_id, offset=offset, limit=100)
        for item in track_data['items']:
            track = item['track']
            if track is not None:
                album = track['album']
                release_date = album['release_date']
                song_id = track['id']
                all_release_date[song_id] = release_date
        if len(track_data['items']) < 100:
            break
        offset += 100  
    return all_release_date

# Sort By Release Date
def sort_playlist(track_list):
    sorted_tracks = dict(sorted(track_list.items(), key=lambda item: item[1]))
    return sorted_tracks

# Create Playlist
def create_playlist(playlist_id):
    json_data = sp.playlist(playlist_id=playlist_id)
    playlist_name = json_data["name"] + " SORTED"
    existing_playlists = get_all_playlists()
    if playlist_name in existing_playlists:
        print("Playlist Already Exists")
        return(None)
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name)
    new_playlist_id = new_playlist["id"]
    return new_playlist_id

# Get All of User's Playlists
def get_all_playlists():
    playlists = []
    json_data = sp.current_user_playlists()
    for item in json_data["items"]:
        playlists.append(item["name"])
    return playlists


# Add Items to Playlist
def add_tracks(playlist_id, tracks_dict):
    track_ids = list(tracks_dict.keys())
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=batch)


# Gets Dictionary of Playlist's Track ID and Track Date
playlist_dict = get_playlist(os.getenv("PLAYLIST_ID"))

# Organizes Playlist's Track ID by Date
sorted_dict = sort_playlist(playlist_dict)

# Creates a New Playlist
new_playlist_id = create_playlist(os.getenv("PLAYLIST_ID"))

# Adds All the Ordered Tracks
if new_playlist_id:
    add_tracks(new_playlist_id, sorted_dict)
else:
    print("Skipped adding tracks as the playlist already exists.")

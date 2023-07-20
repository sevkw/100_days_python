import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(".env.spotify")

BOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# date_input = input("Which date do you want to travel to? Type the date in YYYY-MM-DD: ").split("-")
date_input = "2011-08-28"
music_year = date_input.split("-")[0]

historical_board_url = f"{BOARD_URL}{date_input}"

board_page = requests.get(BOARD_URL).text

soup = BeautifulSoup(board_page, "html.parser")

songs = soup.find_all(name="h3", class_="a-no-trucate")

song_list = [song.text.strip() for song in songs]

## Spotify

sp_scope = ["playlist-modify-private", "playlist-read-private"]

sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=sp_scope)
    )


track_uri_list = []

for song in song_list:
    try:
        result = sp.search(
            q=f"track:{song}:{music_year}",
            limit=1,
            type="track"
        )
        track_uri = result["tracks"]["items"][0]["uri"]
        track_uri_list.append(track_uri)
    except IndexError:
        # print(f"Track:{song} not found, skipped.")
        pass

print(f"{len(track_uri_list)} tracks uri found.")

## https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_create
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_add_tracks

user_id = sp.me()["id"]
play_list_items = sp.user_playlists(user=user_id)["items"]
play_lists = {i["name"]:i["id"] for i in play_list_items}
new_play_list_name = f"{date_input} Billboard 100"

## add the play_list

if new_play_list_name not in play_lists:
    sp.user_playlist_create(
        user=user_id,
        name=new_play_list_name,
        public=False,
        collaborative=False
        )
    
    print(f"A new private playlist {new_play_list_name} has been added!")
    
    new_play_list_items = sp.user_playlists(user=user_id)["items"]
    new_play_lists = {i["name"]:i["id"] for i in new_play_list_items}
    
    # add songs to playlist
    sp.user_playlist_add_tracks(
        user=user_id,
        playlist_id=new_play_lists[new_play_list_name],
        tracks=track_uri_list
    )

    print(f"{len(track_uri_list)} tracks has been added to playlist {new_play_list_name}! Enjoy!")

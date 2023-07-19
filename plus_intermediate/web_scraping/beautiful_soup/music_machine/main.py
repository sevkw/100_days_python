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

# print(historical_board_url)

# songs = soup.select("li h3")
songs = soup.find_all(name="h3", class_="a-no-trucate")

song_list = [song.text.strip() for song in songs]

## Spotify

sp_scope = "playlist-modify-private"

sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=sp_scope)
    )


# user_id = sp.me()["id"]
# user_uri = sp.me()["uri"]
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
        print(f"Track:{song} not found, skipped.")
        pass

print(f"{len(track_uri_list)} tracks uri added.")
print(track_uri_list)
# print(result["tracks"]["items"][0]["album"]["uri"])


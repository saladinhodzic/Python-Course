# SPOTIFY PLAYLIST
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
load_dotenv()

date = input("Which date would you like to travel to?(YYYY-MM-DD) ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/",headers=header)
html = response.text
soup = BeautifulSoup(html,"html.parser")
titles_tags = soup.select(".o-chart-results-list__item h3")
titles = [title.getText().lstrip("\n\n\t\n\t\n\t\t\n\t\t\t\t\t").rstrip("\t\t\n\t\n") for title in titles_tags]

sp= spotipy.Spotify(auth_manager=SpotifyOAuth(
    username="Saladin Hodzic",
    client_id=os.getenv("SPOTIFY_ID"),
    client_secret=os.getenv("SPOTIFY_SECRET"),
    show_dialog=True,
    cache_path="token.txt",
    redirect_uri="https://example.com/",
    scope="playlist-modify-private"
))
user_id = sp.current_user()["id"]
year = date.split("-")[0]
song_uris = []
for title in titles:
    result= sp.search(q=f"track:{title} year:{year}",type="track")
    try:
        uri = result['tracks']["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"That song {title} does not exist on Spotify")
playlist = sp.user_playlist_create(user=user_id,name=f"{date} TOP 100 BILLBOARD",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
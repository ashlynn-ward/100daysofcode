#Spotify Playlist
#Ashlynn Ward, June 25, 2025
#This program looks up Billboard's top 100 songs, and adds them to a Spotify playlist. Note - you must enter your own Spotify info
#for this program to work.

#Import libraries and modules
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Change working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Define constants
#CLIENT_ID = os.environ.get("CLIENT_ID")
#CLIENT_SECRET = os.environ.get("CLEINT_SECRET")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

#Prompt user to enter the year of the songs
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#Define header
header = {
    "User-Agent":"Check https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/ for user agent"
}

#Scrape the top 100 Billboard hits from their website for the correct date
response = requests.get(url = f"https://www.billboard.com/charts/hot-100/{date}", headers = header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

#Get authorization to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="USERNAME", 
    )
)
user_id = sp.current_user()["id"]

#Search for songs in song_name list on Spotify
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Create playlist with songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

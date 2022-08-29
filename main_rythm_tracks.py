from spotifyclient import SpotifyClient
import utils.credentials as credentials
from tqdm import tqdm
from datetime import datetime, timedelta

from models.style import Style
from utils.helper import Helper


spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

# Display all the liked tracks of the user
print("Gathering liked tracks... ", end="", flush=True)
liked_tracks = spotify_client.get_all_liked_tracks()
print("Done")

# Collect audio features for each track and put them in playlists
print("Collecting audio features for each track and putting them in playlists... ", end="", flush=True)
last_years = datetime.today() - timedelta(days=365*3)
tracks = {}
for style in Style:
	tracks[f"{style.name}"] = []

for track in liked_tracks:
	if track.release_date >= last_years:
		track.audio_features = spotify_client.get_audio_features(track)
		track.audio_features.popularity = track.popularity
		for style in Style:
			if Helper.check_style(track, style):
				tracks[f"{style.name}"].append(track)
print("Done")

# Create a playlist for the last 3 years party tracks
print("Creating playlists for the last 3 years tracks for each style... ", end="", flush=True)
for style in Style:
	style_name = style.name.capitalize()
	playlist = spotify_client.create_playlist(f"🤖 {style_name}", f"My liked {style_name} tracks from the last 3 years")
	spotify_client.populate_playlist(playlist, tracks[f"{style.name}"])	
print("Done")
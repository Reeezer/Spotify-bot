from spotifyclient import SpotifyClient
import utils.credentials as credentials
from datetime import datetime, timedelta

from models.track import Track


def create_playlist_for_last_years(years: int, liked_tracks: list[Track]):
    playlist = spotify_client.create_playlist(f"🤖 Last {years} years", f"My liked tracks from the last {years} years")
    last_years = datetime.today() - timedelta(days=365*years)
    tracks = [track for track in liked_tracks if track.release_date >= last_years]
    spotify_client.populate_playlist(playlist, tracks)


spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)


# Display all the liked tracks of the user
print("Gathering liked tracks... ", end="", flush=True)
liked_tracks = spotify_client.get_all_liked_tracks()
print("Done")

# Create a playlist for the last 1 year releases
print("Creating a playlist for the last 1 year releases... ", end="", flush=True)
create_playlist_for_last_years(1, liked_tracks)
print("Done")

# Create a playlist for the last 3 years releases
print("Creating a playlist for the last 3 years releases... ", end="", flush=True)
create_playlist_for_last_years(3, liked_tracks)
print("Done")

# Create a playlist for the last 5 years releases
print("Creating a playlist for the last 5 years releases... ", end="", flush=True)
create_playlist_for_last_years(5, liked_tracks)
print("Done")
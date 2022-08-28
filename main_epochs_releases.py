from spotifyclient import SpotifyClient
import utils.credentials as credentials

from models.track import Track
from utils.helper import Helper


def create_playlist_for_last_years(first_year: int, last_year: int, liked_tracks: list[Track]):
    playlist = spotify_client.create_playlist(f"🤖 {first_year}s", f"My liked tracks from the {first_year}s")
    first_year_date = Helper.str_to_datetime(f"{first_year}-01-01")
    last_year_date = Helper.str_to_datetime(f"{last_year}-01-01")
    tracks = [track for track in liked_tracks if track.release_date >= first_year_date and track.release_date < last_year_date]
    spotify_client.populate_playlist(playlist, tracks)


spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)


# Display all the liked tracks of the user
print("Gathering liked tracks... ", end="", flush=True)
liked_tracks = spotify_client.get_all_liked_tracks()
print("Done")

# Create a playlist for the 1980s releases
print("Creating a playlist for the 1980s releases... ", end="", flush=True)
create_playlist_for_last_years(1980, 1990, liked_tracks)
print("Done")

# Create a playlist for the 1990s releases
print("Creating a playlist for the 1990s releases... ", end="", flush=True)
create_playlist_for_last_years(1990, 2000, liked_tracks)
print("Done")

# Create a playlist for the 2000s releases
print("Creating a playlist for the 2000s releases... ", end="", flush=True)
create_playlist_for_last_years(2000, 2010, liked_tracks)
print("Done")

# Create a playlist for the 2010s releases
print("Creating a playlist for the 2010s releases... ", end="", flush=True)
create_playlist_for_last_years(2010, 2020, liked_tracks)
print("Done")

# Create a playlist for the 2020s releases
print("Creating a playlist for the 2020s releases... ", end="", flush=True)
create_playlist_for_last_years(2020, 2030, liked_tracks)
print("Done")
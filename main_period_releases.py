from spotifyclient import SpotifyClient
import utils.credentials as credentials

from models.track import Track
from utils.helper import Helper


def create_playlist_for_last_years(first_year: int, last_year: int, liked_tracks: list[Track]):
    playlist = spotify_client.create_playlist(f"🤖 {first_year}-{last_year}", f"My liked tracks from the released between {first_year} and {last_year}")
    first_year_date = Helper.str_to_datetime(f"{first_year}-01-01")
    last_year_date = Helper.str_to_datetime(f"{last_year}-01-01")
    tracks = [track for track in liked_tracks if track.release_date >= first_year_date and track.release_date < last_year_date]
    spotify_client.populate_playlist(playlist, tracks)


spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)


# Display all the liked tracks of the user
print("Gathering liked tracks... ", end="", flush=True)
liked_tracks = spotify_client.get_all_liked_tracks()
print("Done")

# Create a playlist for the releases between 2010 and 2015
print("Creating a playlist for the releases between 2010 and 2015... ", end="", flush=True)
create_playlist_for_last_years(2010, 2015, liked_tracks)
print("Done")

# Create a playlist for the releases between 2015 and 2020
print("Creating a playlist for the releases between 2015 and 2020... ", end="", flush=True)
create_playlist_for_last_years(2015, 2020, liked_tracks)
print("Done")
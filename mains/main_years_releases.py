from datetime import datetime, timedelta
import inspect

from models.track import Track
from models.spotifyclient import SpotifyClient
import utils.credentials as credentials


def create_playlist_for_last_years(years: int, liked_tracks: list[Track], spotify_client: SpotifyClient):
    playlist = spotify_client.create_playlist(f"🤖 Last {years} years", f"My liked tracks from the last {years} years")
    last_years = datetime.today() - timedelta(days=365 * years)
    tracks = [track for track in liked_tracks if track.release_date >= last_years]
    spotify_client.populate_playlist(playlist, tracks)


def playlist_from_years_releases(spotify_client: SpotifyClient):
    # Check caller module
    module = inspect.getmodule(inspect.stack()[1][0])
    is_main = __file__ == module.__file__

    # Display all the liked tracks of the user
    if is_main: print("Gathering liked tracks... ", end="", flush=True)
    liked_tracks = spotify_client.get_all_liked_tracks()
    if is_main: print("Done")

    # Create a playlist for the last 1 year releases
    if is_main: print("Creating a playlist for the last 1 year releases... ", end="", flush=True)
    create_playlist_for_last_years(1, liked_tracks, spotify_client)
    if is_main: print("Done")

    # Create a playlist for the last 3 years releases
    if is_main: print("Creating a playlist for the last 3 years releases... ", end="", flush=True)
    create_playlist_for_last_years(3, liked_tracks, spotify_client)
    if is_main: print("Done")

    # Create a playlist for the last 5 years releases
    if is_main: print("Creating a playlist for the last 5 years releases... ", end="", flush=True)
    create_playlist_for_last_years(5, liked_tracks, spotify_client)
    if is_main: print("Done")


if __name__ == "__main__":
    spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)
    
    # Actualize years releases playlists
    playlist_from_years_releases(spotify_client)
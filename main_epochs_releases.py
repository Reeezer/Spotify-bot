import inspect
import re

from models.spotifyclient import SpotifyClient
from models.track import Track
from utils.helper import Helper


def create_playlist_for_last_years(first_year: int, last_year: int, liked_tracks: list[Track], spotify_client: SpotifyClient):
    playlist = spotify_client.create_playlist(f"🤖 {first_year}s", f"My liked tracks from the {first_year}s")
    first_year_date = Helper.str_to_datetime(f"{first_year}-01-01")
    last_year_date = Helper.str_to_datetime(f"{last_year}-01-01")
    tracks = [track for track in liked_tracks if track.release_date >= first_year_date and track.release_date < last_year_date]
    spotify_client.populate_playlist(playlist, tracks)


def playlist_from_epochs_releases(spotify_client: SpotifyClient):
    # Check caller module
    module = inspect.getmodule(inspect.stack()[1][0])
    is_main = __file__ == module.__file__

    # Display all the liked tracks of the user
    if is_main: print("Gathering liked tracks... ", end="", flush=True)
    liked_tracks = spotify_client.get_all_liked_tracks()
    if is_main: print("Done")

    # Create a playlist for every ten years writen in the file
    with open("playlists.txt", "r") as file:
        for line in file:
            result = re.search(r"(\d+)s", line)
            if result:
                first_year = int(result.group(1))
                last_year = first_year + 10
                if is_main: print(f"Creating a playlist for the {first_year}s releases... ", end="", flush=True)
                create_playlist_for_last_years(first_year, last_year, liked_tracks, spotify_client)
                if is_main: print("Done")


if __name__ == "__main__":
    spotify_client = SpotifyClient()
    
    # Actualize epochs releases playlist    
    playlist_from_epochs_releases(spotify_client)
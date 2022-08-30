from datetime import datetime, timedelta
import inspect

from models.spotifyclient import SpotifyClient


def playlist_from_week_releases(spotify_client: SpotifyClient):
    # Check caller module
    module = inspect.getmodule(inspect.stack()[1][0])
    is_main = __file__ == module.__file__

    # Gather followed artists
    if is_main: print("Gathering followed artists... ", end="", flush=True)
    artists = spotify_client.get_all_followed_artists()
    if is_main: print("Done")

    # Gather tracks from every artists that has been made last week
    if is_main: print("Gathering tracks from followed artists that has been released last week... ", end="", flush=True)
    last_week = datetime.today() - timedelta(days=7)
    tracks = []
    for artist in artists:
        albums = spotify_client.get_artist_albums(artist)
        for album in albums:
            if album.release_date >= last_week:
                album_tracks = spotify_client.get_album_tracks(album)
                tracks.extend(album_tracks)
    if is_main: print("Done")

    # Create a playlist for the last week releases
    if is_main: print("Creating a playlist for the last week releases... ", end="", flush=True)
    playlist = spotify_client.create_playlist("🤖 Week's releases", "Tracks released the last week from the artists I like")
    spotify_client.populate_playlist(playlist, tracks)
    if is_main: print("Done")


if __name__ == "__main__":
    spotify_client = SpotifyClient()
    
    # Actualize week's releases playlist    
    playlist_from_week_releases(spotify_client)
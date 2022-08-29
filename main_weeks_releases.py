from spotifyclient import SpotifyClient
import utils.credentials as credentials
from datetime import datetime, timedelta

spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

# Gather followed artists
print("Gathering followed artists... ", end="", flush=True)
artists = spotify_client.get_all_followed_artists()
print("Done")

# Gather tracks from every artists that has been made last week
print("Gathering tracks from followed artists that has been released last week... ", end="", flush=True)
last_week = datetime.today() - timedelta(days=7)
tracks = []
for artist in artists:
    albums = spotify_client.get_artist_albums(artist)
    for album in albums:
        if album.release_date >= last_week:
            album_tracks = spotify_client.get_album_tracks(album)
            tracks.extend(album_tracks)
print("Done")

# Create a playlist for the last week releases
print("Creating a playlist for the last week releases... ", end="", flush=True)
playlist = spotify_client.create_playlist("🤖 Week's releases", "Tracks released the last week from the artists I like")
spotify_client.populate_playlist(playlist, tracks)
print("Done")

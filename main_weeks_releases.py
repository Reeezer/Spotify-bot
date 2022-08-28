from spotifyclient import SpotifyClient
import utils.credentials as credentials
from datetime import datetime, timedelta

spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

# Gather followed artists
artists = spotify_client.get_all_followed_artists()

print(f"{len(artists)} artists followed")
for index, artist in enumerate(artists):
    print(f"{index+1} - {artist}")

# Gather tracks from every artists that has been made last week
print("\nGathering tracks from artists that have been made last week:")
last_week = datetime.today() - timedelta(days=7)
tracks = []
for artist in artists:
    albums = spotify_client.get_artist_albums(artist)
    for album in albums:
        if album.release_date >= last_week:
            print(album)
            album_tracks = spotify_client.get_album_tracks(album)
            tracks.extend(album_tracks)

# Create a playlist for the last week releases
playlist = spotify_client.create_playlist("🤖 Last week", "Tracks from the last week for the artists I like")
spotify_client.populate_playlist(playlist, tracks)

print(f"\nAdding {len(tracks)} tracks from the last week to the playlist...")
for i, track in enumerate(tracks):
    print(f"{i+1} - {track}")
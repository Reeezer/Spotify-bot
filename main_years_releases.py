from spotifyclient import SpotifyClient
import utils.credentials as credentials
from datetime import datetime, timedelta


spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)


# Display all the liked tracks of the user
liked_tracks = spotify_client.get_all_liked_tracks()
print(f"\nHere are the liked tracks of the user:")
for index, track in enumerate(liked_tracks):
    print(f"{index+1} - {track}")


# Create a playlist for the last 1 year releases
playlist = spotify_client.create_playlist("🤖 Last 1 year", "My liked tracks from the last 1 year")

last_year = datetime.today() - timedelta(days=365)
tracks = [track for track in liked_tracks if track.release_date >= last_year]

print(f"\nAdding {len(tracks)} tracks from the last 1 year to the playlist...")
spotify_client.populate_playlist(playlist, tracks)


# Create a playlist for the last 3 years releases
playlist = spotify_client.create_playlist("🤖 Last 3 years", "My liked tracks from the last 3 years")

last_year = datetime.today() - timedelta(days=365*3)
tracks = [track for track in liked_tracks if track.release_date >= last_year]

print(f"\nAdding {len(tracks)} tracks from the last 3 years to the playlist...")
spotify_client.populate_playlist(playlist, tracks)


# Create a playlist for the last 5 years releases
playlist = spotify_client.create_playlist("🤖 Last 5 years", "My liked tracks from the last 5 years")

last_year = datetime.today() - timedelta(days=365*5)
tracks = [track for track in liked_tracks if track.release_date >= last_year]

print(f"\nAdding {len(tracks)} tracks from the last 5 years to the playlist...")
spotify_client.populate_playlist(playlist, tracks)
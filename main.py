from spotifyclient import SpotifyClient
import credentials
from datetime import datetime, timedelta

spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

# Display all the liked tracks of the user
liked_tracks = spotify_client.get_all_liked_tracks()
print(f"\nHere are the liked tracks of the user:")
for index, track in enumerate(liked_tracks):
    print(f"{index+1} - {track}")

# Create a playlist
playlist = spotify_client.create_playlist("🤖 0-1 ans", "My liked tracks from the last year")

# Add the liked tracks from the last year to the playlist
last_year = datetime.today() - timedelta(days=365)
tracks = [track for track in liked_tracks if track.release_date >= last_year]
print(f"\nAdding {len(tracks)} tracks from the last year to the playlist...")
spotify_client.populate_playlist(playlist, tracks)
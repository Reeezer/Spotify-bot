from spotifyclient import SpotifyClient
import utils.credentials as credentials

spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

playlists = spotify_client.get_user_playlists()
for index, playlist in enumerate(playlists):
	print(f"{index+1} - {playlist}")

# Follow every artist that has made a song among the liked tracks
liked_tracks = spotify_client.get_all_liked_tracks()

for track in liked_tracks:
	spotify_client.follow_artist(track.artist)
	print(f"Following {track.artist}")
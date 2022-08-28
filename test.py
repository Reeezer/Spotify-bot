from spotifyclient import SpotifyClient
import credentials

spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

# Display the last 5 tracks played by the user
nb_tracks = 5
last_played_tracks = spotify_client.get_last_played_tracks(nb_tracks)

print(f"Here are the last {nb_tracks} tracks you listened to on Spotify:")
for index, track in enumerate(last_played_tracks):
    print(f"{index+1} - {track}")

# Display the recommended tracks for the last 5 tracks played by the user
recommended_tracks = spotify_client.get_track_recommendations(last_played_tracks, limit=50)
print("\nHere are the recommended tracks from the 5 last listened:")
for index, track in enumerate(recommended_tracks):
    print(f"{index+1} - {track}")

# Create a playlist
playlist_name = "Recommended Tracks"
playlist_description = "Tracks recommended by the Spotify API"
playlist = spotify_client.create_playlist(playlist_name, playlist_description)
print(f"\nPlaylist '{playlist.name}' was created successfully.")

# Populate the playlist with the recommended tracks
spotify_client.populate_playlist(playlist, recommended_tracks)
print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")

# Get the tracks of the playlist
playlist_tracks = spotify_client.get_playlist_tracks(playlist)
print(f"\nHere are the tracks of playlist '{playlist.name}':")
for index, track in enumerate(playlist_tracks):
    print(f"{index+1} - {track}")

# Remove all the tracks of the playlist
spotify_client.remove_tracks_from_playlist(playlist, playlist_tracks)
print(f"\nPlaylist '{playlist.name}' was deleted successfully.")

# Display all the playlists of the user
playlists = spotify_client.get_user_playlists()
print(f"\nHere are the playlists of the user:")
for index, playlist in enumerate(playlists):
    print(f"{index+1} - {playlist}")

# Display the 10 first liked tracks of the user
liked_tracks = spotify_client.get_liked_tracks(limit=10)
print(f"\nHere are the 10 first liked tracks of the user:")
for index, track in enumerate(liked_tracks):
    print(f"{index+1} - {track}")

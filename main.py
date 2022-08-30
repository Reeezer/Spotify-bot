from main_epochs_releases import playlist_from_epochs_releases
from main_period_releases import playlist_from_period_releases
from main_weeks_releases import playlist_from_week_releases
from main_years_releases import playlist_from_years_releases
from main_rythm_tracks import playlist_from_tracks_rythm
from models.spotifyclient import SpotifyClient
import utils.credentials as credentials


if __name__ == "__main__":
    spotify_client = SpotifyClient(credentials.SPOTIFY_AUTHORIZATION_TOKEN, credentials.SPOTIFY_CLIENT_ID)

    # Actualize week's releases playlist
    print("Actualizing week's releases playlist... ", end="", flush=True)
    playlist_from_week_releases(spotify_client)
    print("Done")

	# Actualize years releases playlist
    print("Actualizing years releases playlist... ", end="", flush=True)
    playlist_from_years_releases(spotify_client)
    print("Done")

    # Actualize period releases playlist
    print("Actualizing period releases playlist... ", end="", flush=True)
    playlist_from_period_releases(spotify_client)
    print("Done")

    # Actualize epochs releases playlist
    print("Actualizing epochs releases playlist... ", end="", flush=True)
    playlist_from_epochs_releases(spotify_client)
    print("Done")

    # Actualize tracks rythm playlist
    print("Actualizing tracks rythm playlist... ", end="", flush=True)
    playlist_from_tracks_rythm(spotify_client)
    print("Done")

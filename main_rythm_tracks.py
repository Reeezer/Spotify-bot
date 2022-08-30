from datetime import datetime, timedelta
import inspect

from models.spotifyclient import SpotifyClient
from models.style import Style
from utils.helper import Helper


def playlist_from_tracks_rythm(spotify_client: SpotifyClient):
    # Check caller module
    module = inspect.getmodule(inspect.stack()[1][0])
    is_main = __file__ == module.__file__

    # Gathering all the liked tracks of the user
    if is_main: print("Gathering liked tracks... ", end="", flush=True)
    liked_tracks = spotify_client.get_all_liked_tracks()
    if is_main: print("Done")

    # Gathering all the genres of the artists
    if is_main: print("Gathering all the genres of the artists... ", end="", flush=True)
    for track in liked_tracks:
        for artist in track.artists:
            artist.genres = spotify_client.get_artist_genres(artist)
    if is_main: print("Done")

    # Collect audio features for each track and put them in playlists
    if is_main: print("Collecting audio features for each track and putting them in playlists... ", end="", flush=True)
    last_years = datetime.today() - timedelta(days=365 * 3)
    tracks = {}
    for style in Style:
        tracks[f"{style.name}"] = []

    for track in liked_tracks:
        if track.release_date >= last_years:
            track.audio_features = spotify_client.get_audio_features(track)
            track.audio_features.popularity = track.popularity
            for style in Style:
                if Helper.check_style(track, style):
                    tracks[f"{style.name}"].append(track)
    if is_main: print("Done")

    # Create a playlist for the last 3 years party tracks
    if is_main: print("Creating playlists for the last 3 years tracks for each style... ", end="", flush=True)
    for style in Style:
        style_name = style.name.capitalize()
        playlist = spotify_client.create_playlist(f"🤖 {style_name}", f"My liked {style_name} tracks from the last 3 years")
        spotify_client.populate_playlist(playlist, tracks[f"{style.name}"])
    if is_main: print("Done")


if __name__ == "__main__":
    spotify_client = SpotifyClient()
    
    # Actualize playlists using tracks' rythms
    playlist_from_tracks_rythm(spotify_client)
from models.features import Features
from models.track import Track
from models.playlist import Playlist
from models.artist import Artist
from models.album import Album

class JSON_Handler:
    def list_of_tracks(json_data: dict) -> list[Track]:
        tracks = []
        for track in json_data["items"]:
            track = track["track"]
            artists = JSON_Handler._get_artists(track)
            tracks.append(Track(track["id"], track["name"], artists, track["popularity"], track["album"]["release_date"]))
        return tracks

    def list_of_tracks_recommended(json_data: dict) -> list[Track]:
        tracks = []
        for track in json_data["tracks"]:
            artists = JSON_Handler._get_artists(track)
            tracks.append(Track(track["id"], track["name"], artists, track["popularity"], track["album"]["release_date"]))
        return tracks

    def list_of_tracks_from_album(json_data: dict, album: Album) -> list[Track]:
        tracks = []
        for track in json_data["items"]:
            artists = JSON_Handler._get_artists(track)
            tracks.append(Track(track["id"], track["name"], artists, track["popularity"], album.release_date))
        return tracks

    def list_of_playlists(json_data: dict) -> list[Playlist]:
        playlists = []
        for playlist in json_data["items"]:
            playlists.append(Playlist(playlist["id"], playlist["name"], playlist["description"]))
        return playlists

    def list_of_albums(json_data: dict) -> list[Album]:
        albums = []
        for album in json_data["items"]:
            artists = JSON_Handler._get_artists(album)
            albums.append(Album(album["id"], album["name"], album["type"], artists, album["release_date"], album["total_tracks"]))
        return albums

    def list_of_artists(json_data: dict) -> list[Artist]:
        artists = []
        for artist in json_data["artists"]["items"]:
            genres = JSON_Handler._get_genres(artist)
            artists.append(Artist(artist["id"], artist["name"], genres=genres))
        return artists

    def audio_features(json_data: dict) -> Features:
        return Features(json_data["id"], json_data["danceability"], json_data["energy"], json_data["loudness"], json_data["speechiness"], json_data["acousticness"], json_data["instrumentalness"], json_data["liveness"], json_data["valence"], json_data["tempo"], json_data["key"], json_data["mode"])

    def _get_artists(json_data: dict) -> list[Artist]:
        artists = []
        for artist in json_data["artists"]:
            artists.append(Artist(artist["id"], artist["name"]))
        return artists

    def _get_genres(json_data: dict) -> list[str]:
        genres = []
        for genre in json_data["genres"]:
            genres.append(genre)
        return genres
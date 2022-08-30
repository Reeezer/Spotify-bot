import json
import requests
from enum import Enum
from termcolor import colored
from copy import deepcopy

from models.track import Track
from models.playlist import Playlist
from models.artist import Artist
from models.album import Album
from utils.json_handler import JSON_Handler


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    ##### Construcor #####

    def __init__(self, authorization_token, user_id):
        self._authorization_token = authorization_token
        self._user_id = user_id

    ##### Simple Getters #####

    def get_last_played_tracks(self, limit=10):
        # Get the last N tracks played by the user
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"

        response = self._api_request(url, RequestType.GET)
        tracks = JSON_Handler.list_of_tracks(response.json())

        return tracks

    def get_track_recommendations(self, seed_tracks: list[Track], limit=50):
        # Get a list of recommended tracks starting from a number of seed tracks
        seed_tracks_url = self._tracksurl_from_list(seed_tracks)
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"

        response = self._api_request(url, RequestType.GET)
        tracks = JSON_Handler.list_of_tracks_recommended(response.json())

        return tracks

    def get_user_playlists(self):
        # Get all the playlists of the user
        url = f"https://api.spotify.com/v1/me/playlists"

        response = self._api_request(url, RequestType.GET)
        playlists = JSON_Handler.list_of_playlists(response.json())

        return playlists

    def get_liked_tracks(self, limit=50, offset=0):
        # Get the liked tracks of the user
        url = f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}"

        response = self._api_request(url, RequestType.GET)
        tracks = JSON_Handler.list_of_tracks(response.json())

        return tracks

    def get_playlist_tracks(self, playlist: Playlist, limit=50, offset=0):
        # Get the tracks of a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks?limit={limit}&offset={offset}"

        response = self._api_request(url, RequestType.GET)
        tracks = JSON_Handler.list_of_tracks(response.json())

        return tracks

    def get_album_tracks(self, album: Album):
        # Get all the tracks of an album
        url = f"https://api.spotify.com/v1/albums/{album.id}/tracks"

        if album.type == "album":
            response = self._api_request(url, RequestType.GET)
            tracks = JSON_Handler.list_of_tracks_from_album(response.json(), album)
        elif album.type == "track":
            tracks = [Track(album.id, album.name, album.artists, album.release_date)]

        return tracks

    def get_followed_artists(self, limit=50, after=None):
        # Get all the artists followed by the user
        url = f"https://api.spotify.com/v1/me/following?type=artist&limit={limit}&after={after}" if after else f"https://api.spotify.com/v1/me/following?type=artist&limit={limit}"

        response = self._api_request(url, RequestType.GET)
        artists = JSON_Handler.list_of_artists(response.json())

        return artists

    def get_audio_features(self, track: Track):
        # Get the audio features of a track
        url = f"https://api.spotify.com/v1/audio-features/{track.id}"

        response = self._api_request(url, RequestType.GET)
        features = JSON_Handler.audio_features(response.json())

        return features

    def get_artist_genres(self, artist: Artist):
        # Get the genres of an artist
        url = f"https://api.spotify.com/v1/artists/{artist.id}"

        response = self._api_request(url, RequestType.GET)
        genres = JSON_Handler.list_of_genres(response.json())

        return genres

    ##### Whole Getters #####

    def get_all_liked_tracks(self):
        # Get all the liked tracks of the user
        tracks = []
        offset = 0
        limit = 50

        while True:
            liked_tracks = self.get_liked_tracks(limit=limit, offset=offset)
            tracks += liked_tracks
            if len(liked_tracks) < limit:
                break
            offset += limit

        return tracks

    def get_all_playlist_tracks(self, playlist: Playlist):
        # Get all the tracks of a playlist
        tracks = []
        offset = 0
        limit = 50

        while True:
            playlist_tracks = self.get_playlist_tracks(playlist, limit=limit, offset=offset)
            tracks += playlist_tracks
            if len(playlist_tracks) < limit:
                break
            offset += limit

        return tracks

    def get_all_followed_artists(self):
        # Get all the liked tracks of the user
        artists = []
        after = None
        limit = 50

        while True:
            followed_artists = self.get_followed_artists(limit=limit, after=after)
            artists += followed_artists
            if len(followed_artists) < limit:
                break
            after = followed_artists[-1].id

        return artists

    ##### Setters #####

    def create_playlist(self, name: str, description: str, public=True):
        # Check if the playlist already exists
        user_playlists = self.get_user_playlists()
        for playlist in user_playlists:
            if playlist.name == name:
                self.reset_playlist(playlist)
                return playlist

        # Create a playlist
        url = f"https://api.spotify.com/v1/users/{self._user_id}/playlists"

        data = json.dumps({"name": name, "description": description, "public": public})
        response = self._api_request(url, RequestType.POST, data)
        response_json = response.json()

        playlist = Playlist(response_json["id"], name, description)

        return playlist

    def follow_artist(self, artist: Artist):
        # Follow an artist
        url = f"https://api.spotify.com/v1/me/following?type=artist&ids={artist.id}"
        self._api_request(url, RequestType.PUT)

    def populate_playlist(self, playlist: Playlist, tracks: list[Track]):
        # Add tracks to a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        if len(tracks) == 0:
            return

        tracks_copy = deepcopy(tracks)

        extra_tracks_index = 1
        while extra_tracks_index > 0:
            extra_tracks_index = len(tracks_copy) - 100  # 100 is the maximum number of tracks that can be added at once
            tracks_to_add = tracks_copy[:100]

            data = json.dumps([track.create_spotify_uri() for track in tracks_to_add])
            self._api_request(url, RequestType.POST, data)

            tracks_copy = tracks_copy[100:]
            if extra_tracks_index <= 0:
                break

    ##### Delete #####

    def remove_tracks_from_playlist(self, playlist: Playlist, tracks: list[Track]):
        # Remove tracks from a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        tracks_copy = deepcopy(tracks)

        extra_tracks_index = 1
        while extra_tracks_index > 0:
            extra_tracks_index = len(tracks_copy) - 100  # 100 is the maximum number of tracks that can be removed at once
            tracks_to_remove = tracks_copy[:100]

            data = json.dumps({"tracks": [{"uri": track.create_spotify_uri()} for track in tracks_to_remove]})
            self._api_request(url, RequestType.DELETE, data)

            tracks_copy = tracks_copy[100:]
            if extra_tracks_index <= 0:
                break

    def reset_playlist(self, playlist: Playlist):
        # Delete all the tracks of a playlist
        tracks = self.get_all_playlist_tracks(playlist)
        self.remove_tracks_from_playlist(playlist, tracks)

    def get_artist_albums(self, artist: Artist):
        # Get all the albums of an artist
        url = f"https://api.spotify.com/v1/artists/{artist.id}/albums"

        response = self._api_request(url, RequestType.GET)
        albums = JSON_Handler.list_of_albums(response.json())

        return albums

    ##### Private methods #####

    def _tracksurl_from_list(self, tracks: list):
        tracks_url = ""
        for track in tracks:
            tracks_url += track.id + ","
        tracks_url = tracks_url[:-1]
        return tracks_url

    def _api_request(self, url: str, request_type: RequestType, data=None):
        if request_type == RequestType.GET:
            response = requests.get(url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {self._authorization_token}"})
        elif request_type == RequestType.POST:
            response = requests.post(url, data=data, headers={"Content-Type": "application/json", "Authorization": f"Bearer {self._authorization_token}"})
        elif request_type == RequestType.PUT:
            response = requests.put(url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {self._authorization_token}"})
        elif request_type == RequestType.DELETE:
            response = requests.delete(url, data=data, headers={"Content-Type": "application/json", "Authorization": f"Bearer {self._authorization_token}"})

        if response.status_code < 200 or response.status_code >= 300:
            print(colored(f"\n*** Error while performing the request: {url} ({response.status_code})", "red"))
            print(colored(response.text, "red"))
            exit()

        return response

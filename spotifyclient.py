import json
import requests
from enum import Enum
from termcolor import colored

from track import Track
from playlist import Playlist


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class SpotifyClient:
    """SpotifyClient performs operations using the Spotify API."""

    def __init__(self, authorization_token, user_id):
        self._authorization_token = authorization_token
        self._user_id = user_id

    def get_last_played_tracks(self, limit=10):
        # Get the last N tracks played by the user
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"

        response = self._api_request(url, RequestType.GET)
        response_json = response.json()

        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
        return tracks

    def get_track_recommendations(self, seed_tracks: list[Track], limit=50):
        # Get a list of recommended tracks starting from a number of seed tracks
        seed_tracks_url = self._tracksurl_from_list(seed_tracks)
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"

        response = self._api_request(url, RequestType.GET)
        response_json = response.json()

        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["tracks"]]
        return tracks

    def create_playlist(self, name: str, description: str, public=True):
        # Create a playlist
        url = f"https://api.spotify.com/v1/users/{self._user_id}/playlists"

        data = json.dumps({"name": name, "description": description, "public": public})
        response = self._api_request(url, RequestType.POST, data)
        response_json = response.json()

        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def get_playlist_tracks(self, playlist: Playlist):
        # Get the tracks of a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        
        response = self._api_request(url, RequestType.GET)
        response_json = response.json()
        
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
        return tracks

    def populate_playlist(self, playlist: Playlist, tracks: list[Track]):
        # Add tracks to a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)

        response = self._api_request(url, RequestType.POST, data)
        response_json = response.json()

        return response_json

    def remove_tracks_from_playlist(self, playlist: Playlist, tracks: list[Track]):
        # Delete a playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        data = json.dumps({"tracks": [{"uri": track.create_spotify_uri()} for track in tracks]})
        self._api_request(url, RequestType.DELETE, data=data)

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
            print(colored(f"*** Error while performing the request: {response.status_code}", "red"))
            print(colored(response.text, "red"))
            exit()

        return response

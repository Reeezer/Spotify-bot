import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json 

from utils.helper import scopes

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(), auth_manager=SpotifyOAuth(scope=scopes))

results = spotify.auth_manager.get_access_token(as_dict=False)
print(results)
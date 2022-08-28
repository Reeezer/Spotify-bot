from models.artist import Artist
from utils.helper import Helper

class Album:
    """Artist represents an album of musics or a single"""

    def __init__(self, id: str, name: str, type: str, artists: list[Artist], release_date: str, nb_tracks: int):
        self.name = name
        self.id = id
        self.type = type
        self.artists = artists
        self.release_date = Helper.str_to_datetime(release_date)
        self.nb_tracks = nb_tracks

    def create_spotify_uri(self):
        return f"spotify:album:{self.id}"

    def __str__(self):
        date_str = Helper.datetime_to_str(self.release_date)
        return f"Album: {self.name} by " + ", ".join([artist.name for artist in self.artists]) + f" ({self.type}: {self.nb_tracks} tracks) [{date_str}]"

    def __eq__(self, other):
        if isinstance(other, Album):
            return self.id == other.id
        else:
            return False
            
    def __hash__(self):
        return hash(self.id)

from models.artist import Artist
from utils.helper import Helper

class Track:
    """Track represents a piece of music."""

    def __init__(self, id: str, name: str, artists: list[Artist], release_date: str):
        self.id = id
        self.name = name
        self.artists = artists
        self.release_date = Helper.str_to_datetime(release_date)

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        date_str = Helper.datetime_to_str(self.release_date)
        return f"'{self.name}' by " + ", ".join([artist.name for artist in self.artists]) + f" [{date_str}]"

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.id == other.id
        else:
            return False
            
    def __hash__(self):
        return hash(self.id)

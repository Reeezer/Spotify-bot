class Playlist:
    """Playlist represents a Spotify playlist."""

    def __init__(self, id: str, name: str, description: str):
        self.name = name
        self.id = id
        self.description = description

    def create_spotify_uri(self):
        return f"spotify:playlist:{self.id}"

    def __str__(self):
        return f"Playlist: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Playlist):
            return self.id == other.id
        else:
            return False

    def __hash__(self):
        return hash(self.id)

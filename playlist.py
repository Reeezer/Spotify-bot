class Playlist:
    """Playlist represents a Spotify playlist."""

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Playlist: {self.name}"
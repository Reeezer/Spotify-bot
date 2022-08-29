class Artist:
    """Artist represents a singer or a group of singers."""

    def __init__(self, id: str, name: str, genres: list[str]=None):
        self.name = name
        self.id = id
        self.genres = genres

    def create_spotify_uri(self):
        return f"spotify:artist:{self.id}"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.id == other.id
        else:
            return False
            
    def __hash__(self):
        return hash(self.id)

from datetime import datetime

class Track:
    """Track represents a piece of music."""

    def __init__(self, name: str, id: str, artist: str, release_date: str):
        self.name = name
        self.id = id
        self.artist = artist
        self.release_date = self._to_datetime(release_date)

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        date_str = datetime.strftime(self.release_date, '%Y-%m-%d')
        return f"'{self.name}' by {self.artist} [{date_str}]"

    def _to_datetime(self, string: str):
        formats = ['%Y-%m-%d', '%Y-%m', '%Y']
        for format in formats:
            try:
                dt = datetime.strptime(string, format)
                return dt
            except ValueError:
                pass
        return None

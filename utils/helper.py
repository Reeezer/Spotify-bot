from datetime import datetime
import re

from models.style import Style
from models.artist import Artist


scopes = ["user-top-read", "playlist-read-collaborative", "playlist-modify-public", "playlist-modify-private", "user-library-read", "user-library-modify", "user-follow-read", "user-follow-modify"]


class Helper:
    def str_to_datetime(string: str) -> datetime:
        if isinstance(string, datetime):
            return string

        formats = ["%Y-%m-%d", "%Y-%m", "%Y"]
        for format in formats:
            try:
                dt = datetime.strptime(string, format)
                return dt
            except ValueError:
                pass
        return None

    def datetime_to_str(dt: datetime) -> str:
        if isinstance(dt, str):
            return dt

        return datetime.strftime(dt, "%Y-%m-%d")

    def check_style(track, style: Style) -> bool:
        if track.audio_features is None:
            return False

        for key, value in style.value.items():
            if key == "french":
                for artist in track.artists:
                    if value == True and Helper.is_artist_french(artist):
                        break
                    elif value == False and not Helper.is_artist_french(artist):
                        break
                    return False
            else:
                regex = re.search(r"(min|max)_(\w+)", key)
                sign = regex.group(1)
                feature = regex.group(2)
                if (sign == "min" and track.audio_features.__dict__[feature] < value) or (sign == "max" and track.audio_features.__dict__[feature] > value):
                    return False

        return True

    def is_artist_french(artist: Artist) -> bool:
        if artist.genres is None:
            return False

        for genre in artist.genres:
            if "french" in genre or "francais" in genre or "franc" in genre or "pop urbaine" in genre:
                return True

        return False

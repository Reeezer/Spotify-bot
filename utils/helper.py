from datetime import datetime

from models.style import Style


class Helper:
    def str_to_datetime(string: str) -> datetime:
        if isinstance(string, datetime):
            return string

        formats = ['%Y-%m-%d', '%Y-%m', '%Y']
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
        
        return datetime.strftime(dt, '%Y-%m-%d')

    def check_style(track, style: Style) -> bool:
        if track.audio_features is None:
            return False

        for key, value in style.value.items():
            if track.audio_features.__dict__[key] < value:
                return False
        
        return True
    
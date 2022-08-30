from enum import Enum


class Style(Enum):
    CHILL = {"max_danceability": 0.7, "max_energy": 0.7, "min_valence": 0.2}
    PARTY = {"min_danceability": 0.6, "min_energy": 0.7, "min_popularity": 50, "french": True}

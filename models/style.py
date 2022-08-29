from enum import Enum


class Style(Enum):
    CHILL = {"danceability": 0.4, "energy": 0.5, "loudness": -10, "speechiness": 0.5, "acousticness": 0.5, "instrumentalness": 0.5, "liveness": 0.5, "valence": 0.5, "tempo": 120, "popularity": 60}
    LOVE = {"danceability": 0.2, "energy": 0.5, "loudness": -10, "speechiness": 0.5, "acousticness": 0.5, "instrumentalness": 0.5, "liveness": 0.5, "valence": 0.5, "tempo": 120, "popularity": 60}
    PARTY = {"danceability": 0.7, "energy": 0.6, "popularity": 60, "french": True}
    MOTIVATION = {"danceability": 0.1, "energy": 0.5, "loudness": -10, "speechiness": 0.5, "acousticness": 0.5, "instrumentalness": 0.5, "liveness": 0.5, "valence": 0.5, "tempo": 120, "popularity": 60}
    FOCUS = {"danceability": 0.5, "energy": 0.1, "loudness": -10, "speechiness": 0.5, "acousticness": 0.5, "instrumentalness": 0.5, "liveness": 0.5, "valence": 0.5, "tempo": 120, "popularity": 60}

class Features:
    """Features represents characteristics of a track."""

    def __init__(self, track_id: str, danceability: float, energy: float, loudness: float, speechiness: float, acousticness: float, instrumentalness: float, liveness: float, valence: float, tempo: float, key: int, mode: int):
        self.track_id = track_id
        self.danceability = danceability
        self.energy = energy
        self.loudness = loudness
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.key = key
        self.mode = mode

    def __str__(self):
        return f"Features:\n\tDanceability: {self.danceability}\n\tEnergy: {self.energy}\n\tLoudness: {self.loudness}\n\tSpeechiness: {self.speechiness}\n\tAcousticness: {self.acousticness}\n\tInstrumentalness: {self.instrumentalness}\n\tLiveness: {self.liveness}\n\tValence: {self.valence}\n\tTempo: {self.tempo}\n\tKey: {self.key}\n\tMode: {self.mode}"

    def __eq__(self, other):
        if isinstance(other, Features):
            return self.track_id == other.track_id
        else:
            return False

    def __hash__(self):
        return hash(self.track_id)

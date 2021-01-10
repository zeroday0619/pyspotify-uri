from spotify_uri.util import encode


class Local:
    def __init__(self, artist: str, album: str, track: str, seconds: int) -> None:
        self.artist = artist
        self.album = album
        self.track = track
        self.seconds = seconds

    def toURI(self) -> str:
        return f"spotify:local:{encode(self.artist)}:{encode(self.album)}:{encode(self.track)}:{self.seconds}"

    def toURL(self) -> str:
        return f"/local/{encode(self.artist)}/{encode(self.album)}/{encode(self.track)}/{self.seconds}"

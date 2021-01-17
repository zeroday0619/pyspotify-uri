from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Local(SpotifyUri):
    def __init__(self, uri: str, artist: str, album: str, track: str, seconds: int) -> None:
        self.type = "local"
        self.artist = artist
        self.album = album
        self.track = track
        self.seconds = seconds
        super(Local, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is Local
        if x:
            return v.type == "local"
        else:
            return False

    def toURI(self) -> str:
        return f"spotify:local:{encode(self.artist)}:{encode(self.album)}:{encode(self.track)}:{self.seconds}"

    def toURL(self) -> str:
        return f"/local/{encode(self.artist)}/{encode(self.album)}/{encode(self.track)}/{self.seconds}"

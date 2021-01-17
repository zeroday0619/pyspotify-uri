from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Artist(SpotifyUri):
    def __init__(self, uri: str, _id: str) -> None:
        self.type = 'artist'
        self.id = _id
        super(Artist, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is Artist
        if x:
            return v.type == "artist"
        else:
            return False

    def toURI(self) -> str:
        return f"spotify:{self.type}:${encode(self.id)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.id)}"

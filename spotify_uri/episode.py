from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Episode(SpotifyUri):
    def __init__(self, uri: str, _id: str) -> None:
        self.type = 'episode'
        self.id = _id
        super(Episode, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is Episode
        if x:
            return v.type == "episode"
        else:
            return False

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.id)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.id)}"

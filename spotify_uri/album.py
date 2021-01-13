from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Album(SpotifyUri):
    def __init__(self, uri: str, _id: str) -> None:
        self.type = "album"
        self.id = _id
        super(Album, self).__init__(uri)

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.id)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.id)}"

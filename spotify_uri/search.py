from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Search(SpotifyUri):
    def __init__(self, uri: str, query: str) -> None:
        self.type = "search"
        self.query = query
        super(Search, self).__init__(uri)

    def toURI(self) -> str:
        return f"spotify:search:{encode(self.query)}"

    def toURL(self) -> str:
        return f"/search/{encode(self.query)}"

from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Search(SpotifyUri):
    def __init__(self, uri: str, query: str) -> None:
        self.type = "search"
        self.query = query
        super(Search, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is Search
        if x:
            return v.type == "search"
        else:
            return False

    def toURI(self) -> str:
        return f"spotify:search:{encode(self.query)}"

    def toURL(self) -> str:
        return f"/search/{encode(self.query)}"

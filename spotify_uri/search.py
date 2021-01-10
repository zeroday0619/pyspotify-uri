from spotify_uri.util import encode


class Search:
    def __init__(self, query: str) -> None:
        self.type = "search"
        self.query = query

    def toURI(self) -> str:
        return f"spotify:search:{encode(self.query)}"

    def toURL(self) -> str:
        return f"/search/{encode(self.query)}"

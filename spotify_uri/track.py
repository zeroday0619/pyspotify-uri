from spotify_uri.util import encode


class Track:
    def __init__(self, _id: str) -> None:
        self.type = "track"
        self.id = _id

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.id)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.id)}"

from spotify_uri.util import encode


class User:
    def __init__(self, user: str):
        self.type = "user"
        self.user = user

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.user)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.user)}"

from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class User(SpotifyUri):
    def __init__(self, uri: str, user: str) -> None:
        self.type = "user"
        self.user = user
        super(User, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is User
        if x:
            return v.type == "user"
        else:
            return False

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.user)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.user)}"

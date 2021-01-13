from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class User(SpotifyUri):
    def __init__(self, uri: str, user: str) -> None:
        self.type = "user"
        self.user = user
        super(User, self).__init__(uri)

    def toURI(self) -> str:
        return f"spotify:{self.type}:{encode(self.user)}"

    def toURL(self) -> str:
        return f"/{self.type}/{encode(self.user)}"

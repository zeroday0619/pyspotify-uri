from typing import Any
from spotify_uri.spotify import SpotifyUri
from spotify_uri.util import encode


class Playlist(SpotifyUri):
    def __init__(self, uri: str, _id: str = None, user: str = None) -> None:
        self.type = "playlist"
        self.id = _id
        self.user = user
        super(Playlist, self).__init__(uri)

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is Playlist
        if x:
            return v.type == "playlist"
        else:
            return False

    def toURI(self) -> str:
        if self.user:
            if self.id == "starred":
                return f"spotify:user:{encode(self.user)}:{encode(self.id)}"
            return f"spotify:user:{encode(self.user)}:playlist:{encode(self.id)}"
        return f"spotify:playlist:{encode(self.id)}"

    def toURL(self) -> str:
        if self.user:
            if self.id == "starred":
                return f"/user/{encode(self.user)}/{encode(self.id)}"
            return f"/user/{encode(self.user)}/playlist/{encode(self.id)}"
        return f"/playlist/{encode(self.id)}"

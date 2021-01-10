from spotify_uri.util import encode


class Playlist:
    def __init__(self, _id: str = None, user: str = None):
        self.id = _id
        self.user = user

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

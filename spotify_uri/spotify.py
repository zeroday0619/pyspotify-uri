from typing import Any
from abc import ABC, abstractmethod


class SpotifyUri(ABC):
    def __init__(self, uri: str) -> None:
        self.uri: str = uri

    @abstractmethod
    def toURL(self) -> str:
        pass

    @abstractmethod
    def toURI(self) -> str:
        pass

    @staticmethod
    def is_(v: Any) -> bool:
        x = v is SpotifyUri
        if x:
            return type(v.uri) == str
        else:
            return False

    def toEmbedURL(self) -> str:
        embed_url = f"https://embed.spotify.com/?uri={self.toURI()}"
        return embed_url

    def toOpenURL(self) -> str:
        open_url = f"http://open.spotify.com{self.toURL()}"
        return open_url

    def toPlayURL(self) -> str:
        play_url = f"https://play.spotify.com{self.toURL()}"
        return play_url

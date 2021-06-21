
__version__ = "1.0.2"

from spotify_uri.parse import parse as _parse
from spotify_uri.search import Search as _Search
from spotify_uri.local import Local as _Local
from spotify_uri.playlist import Playlist as _Playlist
from spotify_uri.artist import Artist as _Artist
from spotify_uri.album import Album as _Album
from spotify_uri.track import Track as _Track
from spotify_uri.user import User as _User
from spotify_uri.spotify import SpotifyUri


def parse(uri: str):
    return _parse(uri)


def formatURI(_input: str) -> str:
    _uri: SpotifyUri = parse(_input) if bool(type(_input) == str) else _input
    return _uri.toURI()


def formatEmbedURL(_input: str) -> str:
    _uri: SpotifyUri = parse(_input) if bool(type(_input) == str) else _input
    return _uri.toEmbedURL()


def formatOpenURL(_input: str) -> str:
    _uri: SpotifyUri = parse(_input) if bool(type(_input) == str) else _input
    return _uri.toOpenURL()


def formatPlayURL(_input: str) -> str:
    _uri: SpotifyUri = parse(_input) if bool(type(_input) == str) else _input
    return _uri.toPlayURL()

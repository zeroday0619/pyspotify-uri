__version__ = "1.0.3"

from spotify_uri.parse import parse as _parse
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

from typing import List
from urllib.parse import urlparse, parse_qs
from spotify_uri.local import Local
from spotify_uri.search import Search
from spotify_uri.playlist import Playlist
from spotify_uri.artist import Artist
from spotify_uri.album import Album
from spotify_uri.track import Track
from spotify_uri.episode import Episode
from spotify_uri.user import User
from spotify_uri.util import decode


def parse(_input: str):
    """Parses a "Spotify URI".

    :param _input:
    :type _input: str
    :return:
    :rtype:
    """
    uri = _input
    parsed = urlparse(uri)

    if parsed.hostname == "embed.spotify.com":
        parsedQs = dict(parse_qs(parsed.query))
        return parse(parsedQs.get("uri")[0])

    if parsed.scheme == "spotify":
        parts = uri.split(':')
        return parseParts(uri, parts)

    if parsed.path is None:
        raise TypeError("No pathname")

    parts = parsed.path.split('/')
    return parseParts(uri, parts)


def parseParts(uri: str, parts: List[str]):
    """

    :param uri:
    :type uri:
    :param parts:
    :type parts: List[str]
    :return:
    :rtype:
    """
    length = len(parts)
    if parts[1] == "embed":
        parts = parts[1:]
    if parts[1] == "search":
        return Search(
            uri,
            decode(":".join(parts[:2]))
        )

    if length >= 3 and parts[1] == "local":
        return Local(
            uri,
            decode(parts[2]),
            decode(parts[3]),
            decode(parts[4]),
            int(parts[5])
        )

    if length == 3 and parts[1] == "playlist":
        return Playlist(uri, decode(parts[2]))
    if length == 3 and parts[1] == "user":
        return User(uri, decode(parts[2]))
    if length >= 5:
        return Playlist(uri, decode(parts[4]), decode(parts[2]))
    if length >= 4 and parts[3] == "starred":
        return Playlist(uri, "starred", decode(parts[2]))
    if parts[1] == "artist":
        return Artist(uri, parts[2])
    if parts[1] == "album":
        return Album(uri, parts[2])
    if parts[1] == "track":
        return Track(uri, parts[2])
    if parts[1] == "episode":
        return Episode(uri, parts[2])

    raise TypeError(f"Could not determine type for: {uri}")

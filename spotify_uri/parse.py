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


def parse(input: str):
    uri = input
    parsed = urlparse(url=uri)

    if parsed.hostname == "embed.spotify.com":
        parsedQs = dict(parse_qs(parsed.query))
        return parse(parsedQs.get("uri")[0])

    if parsed.scheme == "spotify:":
        parts = uri.split(':')
        return parseParts(uri=uri, parts=parts)

    if parsed.path is None:
        raise TypeError("No pathname")

    parts = parsed.path.split('/')
    return parseParts(uri=uri, parts=parts)


def parseParts(uri: str, parts: List[str]):
    length = len(parts)
    if parts[1] == "embed":
        parts = parts[:1]

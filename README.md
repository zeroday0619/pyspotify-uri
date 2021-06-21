pyspotify-uri
=============
[![LICENSE](https://img.shields.io/github/license/zeroday0619/pyspotify-uri)](https://github.com/zeroday0619/pyspotify-uri/blob/main/LICENSE)![pyversions](https://img.shields.io/pypi/pyversions/spotify-uri)[![Upload PyPI](https://github.com/zeroday0619/pyspotify-uri/workflows/Upload%20Python%20Package/badge.svg)](https://pypi.org/project/spotify-uri/)

**This project port "[@TooTallNate/spotify-uri](https://github.com/TooTallNate/spotify-uri)" to Python.**

### Parse and format the various Spotify URI formats

Spotify URIs get passed around in a variety of flavors.     
You can also convert them back into Spotify URIs or HTTP URLs.


Installation
------------
```bash
pip install spotify-uri
```

Example
-------
```python
import spotify_uri

# parse Spotify URIs or HTTP URLs:

parsed = spotify_uri.parse("spotify:track:3GU4cxkfdc3lIp9pFEMMmw")
print(parsed.__dict__)
# {
#     'type': 'track', 
#     'id': '3GU4cxkfdc3lIp9pFEMMmw', 
#     'uri': 'spotify:track:3GU4cxkfdc3lIp9pFEMMmw'
# }

parsed = spotify_uri.parse("http://open.spotify.com/track/1pKYYY0dkg23sQQXi0Q5zN")
print(parsed.__dict__)
# {
#     'type': 'track', 
#     'id': '1pKYYY0dkg23sQQXi0Q5zN', 
#     'uri': 'http://open.spotify.com/track/1pKYYY0dkg23sQQXi0Q5zN'
# }


# you can also format the parsed objects back into a URI or HTTP URL:

uri = spotify_uri.formatURI("http://open.spotify.com/track/1pKYYY0dkg23sQQXi0Q5zN")
print(uri)
# spotify:track:1pKYYY0dkg23sQQXi0Q5zN

uri = spotify_uri.formatOpenURL("spotify:track:3GU4cxkfdc3lIp9pFEMMmw")
print(uri)
# http://open.spotify.com/track/3GU4cxkfdc3lIp9pFEMMmw

uri = spotify_uri.formatPlayURL("spotify:track:3GU4cxkfdc3lIp9pFEMMmw")
print(uri)
# https://play.spotify.com/track/3GU4cxkfdc3lIp9pFEMMmw

uri = spotify_uri.formatEmbedURL("spotify:track:3GU4cxkfdc3lIp9pFEMMmw")
print(uri)
# https://embed.spotify.com/?uri=spotify:track:3GU4cxkfdc3lIp9pFEMMmw

```

## License
[MIT](LICENSE)

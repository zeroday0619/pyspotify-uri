
class SpotifyUri:
    @staticmethod
    def toEmbedURL(toURI: str) -> str:
        embed_url = f"https://embed.spotify.com/?uri={toURI}"
        return embed_url

    @staticmethod
    def toOpenURL(toURL: str) -> str:
        open_url = f"http://open.spotify.com{toURL}"
        return open_url

    @staticmethod
    def toPlayURL(toURL: str) -> str:
        play_url = f"https://play.spotify.com{toURL}"
        return play_url

import re
from urllib.parse import unquote
from urllib.parse import quote


def decode(string: str) -> str:
    """URL-decode, also replaces `+` (plus) chars with ` ` (space).

    :param string: encoded url
    :type string: str
    :return: decode url
    :rtype: str
    """
    return re.sub(r"/\+/g", ' ', unquote(string))


def encode(string: str) -> str:
    """

    :param string: decoded url
    :type string: str
    :return: encoded url
    :rtype: str
    """
    return quote(re.sub(r"/ /g", "+", string))

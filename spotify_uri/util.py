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
    a = re.sub(r"/\+/g", ' ', unquote(string))
    return a


def encode(string: str) -> str:
    """

    :param string: decoded url
    :type string: str
    :return: encoded url
    :rtype: str
    """
    d = re.sub(r"/ /g", "+", str(string))
    return quote(str(d))

from urllib.request import urlretrieve
from urllib.parse import ParseResult, urlparse


def queryparse(prased: ParseResult) -> dict:
    return dict(map(lambda x: tuple(x.split('=')), prased.query.split('&')))


def download(url: str, filename: str) -> None:
    urlretrieve(url, filename)

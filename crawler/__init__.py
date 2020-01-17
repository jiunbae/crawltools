import sys
from pathlib import Path

from .spider import Spider
from .webtoon.spiders.webtoon import WebtoonSpider

sys.path.append(str(Path(__file__).parent))

__version__ = '0.1.1'

import scrapy
from tqdm import tqdm

from .utils.beholder import Beholder


class Spider(scrapy.Spider, metaclass=Beholder):
    PREFIX = ''
    POSTFIX ='Spider'

    @classmethod
    def progress(cls, begin, end):
        with tqdm(total=end+1, initial=begin) as tq:
            for index in range(begin, end + 1):
                yield index
                tq.update(1)

    @classmethod
    def _process(cls, name):
        if not name.startswith(cls.PREFIX):
            name = cls.PREFIX + name

        if not name.endswith(cls.POSTFIX):
            name += cls.POSTFIX

        return name.lower().replace('-', '_')

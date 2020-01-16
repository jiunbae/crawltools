import scrapy

from utils.beholder import Beholder


class Spider(scrapy.Spider, metaclass=Beholder):
    PREFIX = ''
    POSTFIX ='Spider'

    @classmethod
    def _process(cls, name):
        if not name.startswith(cls.PREFIX):
            name = cls.PREFIX + name

        if not name.endswith(cls.POSTFIX):
            name += cls.POSTFIX

        return name.lower().replace('-', '_')

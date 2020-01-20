import scrapy
from tqdm import tqdm

from .utils.beholder import Beholder


class Spider(scrapy.Spider, metaclass=Beholder):
    PREFIX = ''
    POSTFIX ='Spider'

    @classmethod
    def progress_init(cls, begin, end):
        cls.progresser = tqdm(total=end, initial=begin)

    @classmethod
    def progress_update(cls, *args, **kwargs):
        cls.progresser.update(1)

    @classmethod
    def _process(cls, name):
        if not name.startswith(cls.PREFIX):
            name = cls.PREFIX + name

        if not name.endswith(cls.POSTFIX):
            name += cls.POSTFIX

        return name.lower().replace('-', '_')

from pathlib import Path

import scrapy

from crawler.spider import Spider
from ..items import WebtoonItem
from utils.url import urlparse, queryparse, download


def arguments(parser):
    parser.add_argument('--id', required=False, default=0, type=int,
                        help="Crawling webtoon id")
    parser.add_argument('--start', required=False, default=1, type=int,
                        help="Crawling webtoon start episode")
    parser.add_argument('--end', required=False, default=-1, type=int,
                        help="Crawling webtoon end episode")


class WebtoonSpider(Spider):
    name = "webtoon"
    ID = 0
    URL_LIST = "https://comic.naver.com/webtoon/list.nhn?titleId={webtoonId}"
    URL = "https://comic.naver.com/webtoon/detail.nhn?titleId={webtoonId}&no={webtoonIndex}"

    def start_requests(self):
        self.ID = str(self.settings.get('id'))
        yield scrapy.Request(self.URL_LIST.format(webtoonId=self.ID), callback=self.parse_init)

    def parse_init(self, response):
        dest = Path(self.ID)

        latest = next(iter(response.xpath("//td[@class='title']/a/@href")), None)

        if latest is None:
            raise RuntimeError(f"{self.ID} is not valide webtoon id!")

        latest = int(queryparse(urlparse(latest.extract())).get('no', 0))
        
        webtoonStart = self.settings.get('start')
        webtoonEnd = self.settings.get('end')

        if webtoonEnd == -1 or webtoonEnd > latest:
            webtoonEnd = latest

        for index in range(webtoonStart, webtoonEnd + 1):
            yield scrapy.Request(url=self.URL.format(webtoonId=self.ID, webtoonIndex=index),
                                 callback=self.parse, meta={'path': str(dest.joinpath(f'{index:06}'))})

    def parse(self, response):
        for index, src in enumerate(map(scrapy.Selector.extract, 
                                        response.xpath("//div[@class='wt_viewer']//img/@src"))):
            yield WebtoonItem(image_urls=[src], 
                              image_names=[f'{response.meta["path"]}-{index}{Path(src).suffix}'])

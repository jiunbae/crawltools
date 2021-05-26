from pathlib import Path
from itertools import chain

import scrapy

from crawltools.spider import Spider
from crawltools.utils.url import urlparse, queryparse, download
from ..items import ComicItem

def arguments(parser):
    parser.add_argument('--url', required=False, default="manatoki95.net", type=str,
                        help="Manatoki URL prefix")

    parser.add_argument('--id', required=False, default=0, type=int,
                        help="Crawling comic id")
    parser.add_argument('--skip', required=False, action='store_true', default=False,
                        help="Skip if exists")


class ManatokiSpider(Spider):
    name = "manatoki"
    ID = 0
    BASE_URL = "manatoki95.net"
    URL_LIST = "https://{base_url}/comic/{comic_id}"
    URL_ITEM = "https://{base_url}/comic/{comic_index}"

    def start_requests(self):
        self.ID = str(self.settings.get('id'))
        self.BASE_URL = str(self.settings.get('url'))
        
        yield scrapy.Request(
            self.URL_LIST.format(base_url=self.BASE_URL, comic_id=self.ID),
            callback=self.parse_init
        )

    def parse_init(self, response):
        comic_name = response.xpath('//span[@class="page-desc"]/text()').extract_first().strip()
        comic_items = tuple(response.xpath('//li[@class="list-item"]//a[@class="item-subject"]'))

        if not comic_items:
            raise RuntimeError(f"{self.ID} is not valide manatoki comic!")

        self.progress_init(0, len(comic_items))
        for item in comic_items:
            item_name, *_ = filter(len, chain(*map(str.splitlines, item.xpath('text()').extract())))
            item_href = item.xpath('@href').extract_first()
            
            yield scrapy.Request(
                url=item_href,
                meta={'path': f'{comic_name}/{item_name}'},
                callback=self.parse,
            )

    def parse(self, response):
        try:
            script = response.xpath("//script[contains(., 'html_encoder(html_data);')]/text()").extract_first()
            context = ''.join(map(
                lambda line: line[line.index("'")+1:line.rindex("'")],
                filter(lambda x: x.startswith("html_data+="), script.splitlines())
            ))
            context = scrapy.Selector(text=''.join(map(
                lambda x: chr(int(x, 16)),
                filter(len, context.split('.'))
            )))

            image_urls = []
            for elements in context.xpath('//div'):
                for element in elements.xpath('//img').extract():
                    if '/img/loading-image.gif' in element:
                        image_urls.append(element.split('data-')[1].split('\"')[1])

            image_names = [
                f'{response.meta["path"]}/{i:06}{Path(image_url).suffix}'
                for i, image_url in enumerate(image_urls)
            ]

            yield ComicItem(
                image_urls=image_urls,
                image_names=image_names,
                image_downloaded=[False] * len(image_urls)
            )

        except ValueError:
            pass

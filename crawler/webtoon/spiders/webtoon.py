import scrapy

from crawler.spider import Spider


def arguments(parser):
    parser.add_argument('--id', required=True, default=0, type=int,
                        help="evaluate only, not detecting")
    parser.add_argument('--start', required=False, default=1, type=int,
                        help="Crawling webtoon start episode")
    parser.add_argument('--end', required=False, default=-1, type=int,
                        help="Crawling webtoon end episode")


class WebtoonSpider(Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

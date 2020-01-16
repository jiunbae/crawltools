import scrapy
from scrapy.crawler import CrawlerProcess

from utils.arguments import Arguments
from crawler import Spider


if __name__ == "__main__":
    arguments = Arguments()

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(Spider.get('webtoon'))
    process.start()

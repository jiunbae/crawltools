import scrapy
from scrapy.crawler import CrawlerProcess

from crawler import Spider

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(Spider.get('webtoon'))
    process.start()

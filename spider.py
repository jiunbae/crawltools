import sys
import scrapy
from scrapy.crawler import CrawlerProcess

from utils.arguments import Arguments
from crawler import Spider


def main(args: Arguments.parse.Namespace):
    process = CrawlerProcess(vars(args))

    process.crawl(Spider.get(args.command))
    process.start()

if __name__ == "__main__":
    main(Arguments())

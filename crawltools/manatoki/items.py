# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    images = scrapy.Field()

    image_urls = scrapy.Field()
    image_names = scrapy.Field()
    image_downloaded = scrapy.Field()

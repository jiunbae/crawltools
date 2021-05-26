# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ComicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for index, (image_url, image_name) in enumerate(zip(item['image_urls'], item['image_names'])):
            yield scrapy.Request(
                image_url,
                meta={
                    'name': image_name,
                    'index': index,
                    'item': item, 
                },
            )

    def file_path(self, request, response=None, info=None):
        return request.meta['name']

    def item_completed(self, results, item, info):
        self.spiderinfo.spider.progress_update()

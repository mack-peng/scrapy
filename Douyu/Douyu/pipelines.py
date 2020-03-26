# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from Douyu.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image_link = item['image_link']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        if not image_path:
            raise image_path("Item contains no files")
        os.rename(images_store + image_path[0], images_store + item['nickname'] + ".jpg")
        item['image_paths'] = image_path
        return item


    #def process_item(self, item, spider):
    #   return item





class ImagespiderPipeline(ImagesPipeline):

    def get_media_request(self, item, info):
        for image_url in item['imgurl']:
            yield scrapy.Request(url=image_url)

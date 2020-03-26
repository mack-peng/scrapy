# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class UgirlsportraitPipeline(object):
    def process_item(self, item, spider):
        return item


# 定义图片处理管道
class UgirlsportraitImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_urls']:
            yield scrapy.Request(url=image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 注意，这里是request
        item = request.meta['item']
        item = dict(item)
        img_type = item['img_type']
        img_type_strip = img_type.strip()
        folder = item['name']
        folder_strip = folder.strip()
        image_guid = request.url.split('/')[-1]
        filename = u'{0}/{1}/{2}'.format(img_type_strip, folder_strip, image_guid)
        return filename
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        folder = request.url.split('/')[-2]
        folder_strip = folder.strip()
        image_guid = request.url.split('/')[-1]
        filename = u'imge/{0}/{1}'.format(folder_strip, image_guid)
        return filename

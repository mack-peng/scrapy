# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import csv
import os
from scrapy.pipelines.images import ImagesPipeline

if not os.path.exists("./output"):
    os.makedirs("./output")


class UgirlsPipeline(object):

    def open_spider(self, spider):
        # 开启时执行的方法
        f = open('./output/ugril.csv', 'w+', encoding="utf-8")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["name", "index_url", "location", "head_portrait", "three_circlfes", "number"
                                , "description", "popularity", "fans", "album", "video"])
        self.f = f
        self.csv_writer = csv_writer

    def process_item(self, item, spider):
        dict_item = dict(item)
        write_row = []
        write_row.append(dict_item['name'])
        write_row.append(dict_item['index_url'])
        write_row.append(dict_item['head_portrait'])
        write_row.append(dict_item['location'])
        write_row.append(dict_item['three_circlfes'].replace("-", "/"))
        write_row.append(dict_item['description'])
        write_row.append(dict_item['popularity'])
        write_row.append(dict_item['fans'])
        write_row.append(dict_item['album'])
        write_row.append(dict_item['video'])
        self.csv_writer.writerow(write_row)
        # 告诉本次item处理完成，必须返回，其他管道可继续处理
        return item

    # 爬虫结束时候执行
    def close_spider(self, spider):
        self.f.close()


# 定义图片处理管道
class UgirlsImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_urls']:
            yield scrapy.Request(url=image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # 注意，这里是request
        item = request.meta['item']
        item = dict(item)
        type_path = item['save_path_name']
        type_path = type_path.strip()

        folder = item['number']
        folder_strip = folder.strip()
        image_guid = request.url.split('/')[-1]
        filename = u'{0}/{1}/{2}'.format(type_path, folder_strip, image_guid)
        return filename

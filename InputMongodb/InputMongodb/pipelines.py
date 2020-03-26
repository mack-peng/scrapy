# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# 建立MongoDb数据库连接
# client = pymongo.MongoClient('127.0.0.1', 27017)
# # 连接所需数据库，ScrapyChina为数据库名
# db = client['ScrapyChina']
# # 连接所用集合，也就是我们通常所说的表，mingyan为表名
# db_name = db['mingyan']
# client.close()
# exit()

class InputmongodbPipeline(object):

    def __init__(self):
        # 建立MongoDb数据库连接
        client = pymongo.MongoClient('127.0.0.1', 27017)
        self.mongo_client = client
        # 连接所需数据库，ScrapyChina为数据库名
        db = client['ScrapyChina']
        # 连接所用集合，也就是我们通常所说的表，mingyan为表名
        self.post = db['mingyan']

    def process_item(self, item, spider):
        postItem = dict(item)
        self.post.insert(postItem)
        return item

    def close_spider(self, spider):
        self.mongo_client.close()

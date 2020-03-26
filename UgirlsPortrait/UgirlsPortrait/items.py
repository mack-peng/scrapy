# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UgirlsportraitItem(scrapy.Item):
    # name
    name = scrapy.Field()
    # img_urls
    img_urls = scrapy.Field()
    # 分类
    img_type = scrapy.Field()
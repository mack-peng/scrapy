# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UgirlsItem(scrapy.Item):
    # 存放到不同目录
    save_path_name = scrapy.Field()
    # 首页url
    index_url = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 头像url
    head_portrait = scrapy.Field()
    # number
    number = scrapy.Field()
    # 城市
    location = scrapy.Field()
    # 身高
    height = scrapy.Field()
    # 三维
    three_circlfes = scrapy.Field()
    # 简介
    description = scrapy.Field()
    # 人气
    popularity = scrapy.Field()
    # 粉丝
    fans = scrapy.Field()
    # 专辑
    album = scrapy.Field()
    # 视频
    video = scrapy.Field()
    # 微博
    wei_blog = scrapy.Field()
    # 图片连接列表
    img_urls = scrapy.Field()



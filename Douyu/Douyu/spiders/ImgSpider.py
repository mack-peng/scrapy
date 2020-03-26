# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem() # ÊµÀý»¯item
        imgurls = response.css(".post img::attr(src)").extruct()
        item['imageurl'] = imgurls
        yield item

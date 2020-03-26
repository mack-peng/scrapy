# -*- coding: utf-8 -*-
"""
    ugirls 中的美女写真栏目图片
"""
import scrapy
from Ugirls.items import UgirlsItem


class BeautyPortraitSpider(scrapy.Spider):
    name = 'BeautyPortrait'
    allowed_domains = ['ugirls.fm']
    next_page_base = "https://www.ugirls.fm/Index/Search/"
    start_urls = [
        "https://www.ugirls.fm/Index/Search/Magazine-64.html",
        "https://www.ugirls.fm/Index/Search/Magazine-71.html",
        'https://www.ugirls.fm/Index/Search/Magazine-104.html',
        "https://www.ugirls.fm/Index/Search/Magazine-102.html",
        "https://www.ugirls.fm/Index/Search/Magazine-59.html",
        "https://www.ugirls.fm/Index/Search/Magazine-86.html",
        "https://www.ugirls.fm/Index/Search/Magazine-19.html",
        "https://www.ugirls.fm/Index/Search/Magazine-58.html",
        "https://www.ugirls.fm/Index/Search/Magazine-57.html",
        "https://www.ugirls.fm/Index/Search/Magazine-55.html",
        "https://www.ugirls.fm/Index/Search/Magazine-54.html",
        "https://www.ugirls.fm/Index/Search/Magazine-53.html",
        "https://www.ugirls.fm/Index/Search/Magazine-51.html",
        "https://www.ugirls.fm/Index/Search/Magazine-50.html",
    ]

    # 第一层处理
    def parse(self, response):
        img_panels = response.css(".magazine_wrap")
        # 判断是否存在下一页
        next_tag = response.css(".xfenye img::attr(src)").extract()
        if len(next_tag) > 0 and next_tag[-1] == "/images/xlist_aaaBg.png":
            next_page = response.css(".xfenye a::attr(href)").extract()[-1]
        else:
            next_page = ""


        for img_panel in img_panels:
            img_url = img_panel.css("a::attr(href)").extract_first()
            item = UgirlsItem()
            item['number'] = img_panel.css("a::attr(title)").extract_first()
            item['save_path_name'] = response.url.split("/")[-1].rstrip(".html")
            yield scrapy.Request(url=img_url, callback=self.parse_detail, meta={'item': item})

        if next_page:
            yield scrapy.Request(url=str(self.next_page_base) + str(next_page), callback=self.parse)

    # 第二层处理
    def parse_detail(self, response):
        item = response.meta['item']
        img_urls_web_m = response.css(".scaleimg::attr(src)").extract()
        img_urls = []
        for img_url in img_urls_web_m:
            img_url = img_url.replace("_magazine_web_m", "")
            img_urls.append(img_url)
        item['img_urls'] = img_urls
        yield item


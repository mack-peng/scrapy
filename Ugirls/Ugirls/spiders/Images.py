# -*- coding: utf-8 -*-
import scrapy
from Ugirls.items import UgirlsItem


class ImagesSpider(scrapy.Spider):
    name = 'Images'
    allowed_domains = ['ugirls.fm']
    start_urls = [
        "https://www.ugirls.fm/Models/siwa.html",
        "https://www.ugirls.fm/Models/rehuo.html",
        'https://www.ugirls.fm/Models/nenmo.html',
        "https://www.ugirls.fm/Models/sifangyouhuo.html",
        "https://www.ugirls.fm/Models/xingganyouwu.html",
        "https://www.ugirls.fm/Models/quxian.html",
        "https://www.ugirls.fm/Models/nvwangfaner.html",
        "https://www.ugirls.fm/Models/bijini.html",
        "https://www.ugirls.fm/Models/rixi.html",
    ]

    # 第一层处理
    def parse(self, response):
        img_panels = response.css(".model_item.rectangle")
        for img_panel in img_panels:
            item = UgirlsItem()
            # 内页的网址
            img_url = img_panel.css("a::attr(href)").extract_first()
            item['save_path_name'] = response.url.split("/")[-1].rstrip(".html")
            item['name'] = img_panel.css(".model_name::text").extract_first()
            item['location'] = img_panel.css(".model_location::text").extract_first()
            item['three_circlfes'] = img_panel.css(".model_measurement::text").extract_first()
            item['number'] = img_panel.css(".model_latest_magazine_name::text").extract_first()

            if img_url:
                yield scrapy.Request(url=img_url, callback=self.parse_detail, meta={'item': item})


    # 第二层处理
    def parse_detail(self, response):
        item = response.meta['item']
        img_urls_web_m = response.css("#myGallery img::attr(src)").extract()
        img_urls = []
        for temp_url in img_urls_web_m:
            img_url = temp_url.replace("_magazine_web_m", "")
            img_urls.append(img_url)

        # 处理成高清图数据链接
        item['img_urls'] = img_urls
        # 头像
        item['head_portrait'] =  response.css(".ren_head .photo img::attr(src)").extract_first()
        # 首页
        item['index_url'] = response.css(".ren_head .photo::attr(href)").extract_first()
        # 简介
        item['description'] = response.css(".ren_head").xpath("p[3]/text()").extract_first()
        # 人气
        item['popularity'] = response.css(".ren_info strong::text").extract_first()
        # 粉丝
        item['fans'] = response.css(".ren_info").xpath("a[1]/text()").extract_first()
        # 专辑
        item['album'] = response.css(".ren_info").xpath("a[2]/text()").extract_first()
        # 视频
        item['video'] = response.css(".ren_info").xpath("a[3]/text()").extract_first()

        # 微博
        item['wei_blog'] = response.css(".ren_url a::attr(href)").extract_first()
        if item['wei_blog'] == 'javascript:void(0)':
            item['wei_blog'] = ""

        yield item


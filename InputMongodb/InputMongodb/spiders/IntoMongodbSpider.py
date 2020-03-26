# -*- coding: utf-8 -*-
import scrapy
from InputMongodb.items import InputmongodbItem

class IntomongodbspiderSpider(scrapy.Spider):
    name = 'IntoMongodbSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css('div.quote')

        item = InputmongodbItem()

        for v in mingyan:
            item['cont'] = v.css('.text::text').extract_first()
            # 提取名言
            tags = v.css('.tags .tag::text').extract()
            # 数组转换为字符串
            item['tag'] = ','.join(tags)
            # 把提取到的数据提交给pipline处理
            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        # 判断是否存在下一页
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # 提交给parse继续抓取下一页
            yield scrapy.Request(next_page, callback=self.parse)


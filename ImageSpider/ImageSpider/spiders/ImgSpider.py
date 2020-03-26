import scrapy
from ImageSpider.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['tom631.com']
    base_url = "https://tom631.com/"
    start_urls = ['https://tom631.com/meinvxiezhen/index_2.html']
    page_count = 1

    # 第一层处理
    def parse(self, response):
        img_urls = response.css(".tuijian-tupian::attr(href)").extract()
        page_html = response.css(".page-select-box .ye .ye1 .span1")
        if len(page_html) > 2:
            next_page =  response.css(".page-select-box .ye .ye1 .span1")[2].css("a::attr(href)").extract()[0]
        else:
            next_page = ''

        for url in img_urls:
            yield scrapy.Request(url=self.base_url + url, callback=self.parse_detail)

        self.page_count += 1
        # 只下载10页
        if next_page and self.page_count < 10:
            yield scrapy.Request(url=self.base_url + next_page, callback=self.parse)


    # 解析二级子页面
    def parse_detail(self, response):
        img_urls = response.css(".xiezhen img::attr(src)").extract()
        item = ImagespiderItem()
        item['imgurl'] = img_urls
        yield item

# scrapy
scrapy Reptile framework practice

---------
- Douyu
    - 斗鱼主播接口爬取
    - 目的：爬取主播基本信息数据
    - 运行命令：scrapy crawl douyu
    
---------
- tom
    - tom影院图片爬取
    - 保存位置设置 settings.IMAGES_STORE
    - 运行命令：scrapy crawl ImgSpider
    
--------
- InputMongodb
    - 爬取数据并保存到mongodb中
    - 爬取网站[http://lab.scrapyd.cn/]
    - 运行命令：scrapy crawl IntoMongodbSpider

-----------
- Ugirls
    - 目的
        - 爬取尤果网中 【性感尤物】栏目所有分类下的展示模特和内页图片（6张）
        - 获取美女基本数据保存到 ./output/ugril.csv中，用作数据分析
    - 爬取地址["https://www.ugirls.fm/Models]
    - 保存位置设置 settings.IMAGES_STORE
    - 输出.csv文件位置 执行位置 ./output/ugril.csv
    - 运行命令：scrapy crawl Images

------
- UgirlsPortrait
    - 目的
        - 爬取尤果网中 【美女写真】栏目所有分类下的展示模特和内页图片（6张）
    - 爬取地址[https://www.ugirls.fm/Content/]
    - 保存位置设置 settings.IMAGES_STORE
    - 运行命令：scrapy crawl portrait

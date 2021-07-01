import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/frim/index1.html']

    # 创建Redis链接对象
    conn = Redis(
        host='127.0.0.1',
        port=6379
    )

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
        # href="/frim/index1-3.html"
    )

    # 对每一页进行数据解析，请求电影详情页的url
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            detail_url = 'https://www.4567tv.tv/' + li.xpath('./div/a/@href').extract_first()
            # 将详情页的url存入redis的set中
            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('该url没有被爬取过，可以进行数据的爬取')
                yield scrapy.Request(url=detail_url,callback=self.parse_detail)
            else:
                print('数据还没有更新，暂无数据可以爬取！')

    # 解析电影详情的名字和简介
    def parse_detail(self,respose):
        item = MovieproItem()
        name = respose.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        intro = respose.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['name'] = name
        item['intro'] = intro
        yield item
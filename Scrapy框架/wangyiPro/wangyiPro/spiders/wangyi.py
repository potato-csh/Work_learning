import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储五大板块对应详情页的url

    # 实例化一个对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'C:\Users\Potato\Documents\chromedriver')

    # 解析五大板块的url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [2, 3, 5, 6, 7]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        # 对每一个板块的页面进行请求
        for url in self.models_urls:
            # 对每一个板块的url进行请求发送
            yield scrapy.Request(url=url, callback=self.model_parse)

    # 由于每一个板块的对应的新闻都是动态加载的
    def model_parse(self, response):
        # 解析每一个板块页面中新闻的标题和新闻详情页的url
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div.div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            # 对新闻详情页的url发送请求
            yield scrapy.Request(url=new_url, callback=self.detail_parse, meta={'item': item})

    # 解析详情新闻页的内容
    def detail_parse(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self, spider):
        self.bro.quit()

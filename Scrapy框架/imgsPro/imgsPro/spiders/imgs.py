import scrapy
from imgsPro.items import ImgsproItem


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 使用伪属性
            src = 'https:' + div.xpath('./div/a/img/@src2').extract_first()

            item = ImgsproItem()
            item['src'] = src

            yield item

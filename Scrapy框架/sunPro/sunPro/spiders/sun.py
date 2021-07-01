import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']

    # 链接提取器：根据指定规则(allow="正则")进行指定链接的提取
    link = LinkExtractor(allow=r'id=\d+&page=\d+')
    # https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1
    # https://wz.sun0769.com/political/index/politicsNewest?id=1&page=2

    detail_link = LinkExtractor(allow=r'politics\/index\?id=\d+')
    # https://wz.sun0769.com/political/politics/index?id=507609
    # https://wz.sun0769.com/political/politics/index?id=507595

    rules = (
        # 规则解析器：将链接提取器提取到的链接进行制定规则(callback)的解析操作
        Rule(link, callback='parse_item', follow=True),
        # follow=True：可以将链接提取器 继续作用到 链接提取器提取的链接 所对应的页面中
        Rule(detail_link,callback='parse_detail')
    )

    # 解析问政编号和问政标题
    def parse_item(self, response):

        li_list = response.xpath('/html//div[2]/div[3]/ul[2]/li')
        for li in li_list:
            code = li.xpath('./span[1]/text()').extract_first()
            title = li.xpath('./span[3]/a/text()').extract_first()
            item = SunproItem()
            item['code'] = code
            item['title'] = title
            yield item

    # 解析问政详情页的编号和内容
    def parse_detail(self,response):
        code_detail = response.xpath('/html//div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        content = response.xpath('/html//div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item = DetailItem()
        item['code_detail'] = code_detail
        item['content'] = content
        yield item



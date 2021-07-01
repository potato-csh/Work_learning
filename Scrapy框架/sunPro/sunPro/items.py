# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    title = scrapy.Field()


class DetailItem(scrapy.Item):
    # define the fields for your item here like:
    code_detail = scrapy.Field()
    content = scrapy.Field()

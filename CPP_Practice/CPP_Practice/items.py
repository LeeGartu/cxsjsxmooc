# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CppPracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 爬取对象：描述，输入，输出，样例输入，样例输出
    test_title = scrapy.Field()
    test_describe = scrapy.Field()
    test_input = scrapy.Field()
    test_output = scrapy.Field()
    demo_input = scrapy.Field()
    demo_output = scrapy.Field()

    pass

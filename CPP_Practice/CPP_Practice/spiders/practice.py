# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from CPP_Practice.items import CppPracticeItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class PracticeSpider(scrapy.Spider):
    name = 'practice'
    allowed_domains = ['cxsjsxmooc.openjudge.cn']
    start_urls = ['http://cxsjsxmooc.openjudge.cn/2020t3fallall']

    def parse(self, response):
        url_list = response.xpath('//*[@class="problem-id"]//@href').extract()

        for url in url_list:
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

    def parse_detail(self, response):
        print('\n' * 5)


        test_title = response.xpath('//*[@id="pageTitle"]/h2/text()').get()
        test_describe = response.xpath(
            '//*[@id="pagebody"]/div/div[3]/dl[2]/dd[1]/p/text()').get()
        test_input = response.xpath(
            '//*[@id="pagebody"]/div/div[3]/dl[2]/dd[2]/text()').get()
        test_output = response.xpath(
            '//*[@id="pagebody"]/div/div[3]/dl[2]/dd[3]/text()').get()
        demo_input = response.xpath(
            '//*[@id="pagebody"]/div/div[3]/dl[2]/dd[4]/pre/text()').get()
        demo_output = response.xpath(
            '//*[@id="pagebody"]/div/div[3]/dl[2]/dd[5]/pre/text()').get()

        items = CppPracticeItem(test_title=test_title,
                                test_describe=test_describe,
                                test_input=test_input,
                                test_output=test_output,
                                demo_input=demo_input,
                                demo_output=demo_output)
        # items = CppPracticeItem(test_title,
        #                         test_describe,
        #                         test_input,
        #                         test_output,
        #                         demo_input,
        #                         demo_output)

        yield items

        print('\n' * 5)

        pass

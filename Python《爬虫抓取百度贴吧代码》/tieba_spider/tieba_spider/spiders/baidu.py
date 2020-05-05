# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from tieba_spider.items import TiebaItem



class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E9%98%B2%E8%AF%88%E9%AA%97']

    def parse(self, response):
        # 获取帖子中的url
        url_list = response.css('.j_th_tit::attr(href)').extract()

        # 挨个的url进行访问
        for url in url_list:
            yield scrapy.Request(url=parse.urljoin(response.url, url), callback=self.parse_detail)

        # 定位到下一页，并翻页
        next_url = response.css(".next.pagination-item::attr(href)").extract()[0]

        if next_url:
            yield scrapy.Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    # 详情页面解析
    def parse_detail(self,response):
        print(response.url)
        title = response.css(".core_title_txt.pull-left.text-overflow::text").extract()
        if title:
            # 定位作者
            authors = response.css(".p_author_name.j_user_card::text").extract()

            # 定位帖子内容
            contents_list = response.css(".d_post_content.j_d_post_content").extract()

            bbs_sendtime_list,bbs_floor_list = self.get_sendtime_and_floor(response)

            # 执行数据的存储
            for i in range(len(authors)):
                tieba_item = TiebaItem()
                tieba_item["title"] = title[0]
                tieba_item["author"] = authors[i]
                tieba_item["content"] = contents_list[i]
                tieba_item["reply_time"] = bbs_sendtime_list[i]
                tieba_item["floor"] = bbs_floor_list[i]

                yield tieba_item




    def get_sendtime_and_floor(self,response):
        bbs_sendtime_and_floor_list = response.css(".post-tail-wrap span[class=tail-info]::text").extract()

        i = 0
        bbs_sendtime_list = []
        bbs_floor_list = []

        for lz in bbs_sendtime_and_floor_list:
            if lz == "来自":
                bbs_sendtime_and_floor_list.remove(lz)

        for bbs_sendtime_and_floor in bbs_sendtime_and_floor_list:
            # 获取帖子位于的楼数
            if i % 2 == 0:
                bbs_floor_list.append(bbs_sendtime_and_floor)

            # 获取发帖时间
            if i % 2 == 1:
                bbs_sendtime_list.append(bbs_sendtime_and_floor)

            i += 1
        return bbs_sendtime_list, bbs_floor_list
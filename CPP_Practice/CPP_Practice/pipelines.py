# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv

class CppPracticePipeline:
    def __init__(self):
        self.fp = open("CPP_PRACTICE_THREE",'w',encoding= 'utf-8')


    def open_spider(self, spider):
        print("爬虫开始。。。")
        pass
    
    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json + '\n')
        # csv.writer(self.fp).writerow(dict(item))
        
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束。。。")
        pass

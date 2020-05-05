__author__ = "zhou"
__date__ = "2019-09-05 20:41"

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "baidu"])


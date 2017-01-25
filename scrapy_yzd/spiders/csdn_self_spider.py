# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import DoubanItem

class csdn_selfSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/qqxx6661/article/details/52083332",
        "http://blog.csdn.net/qqxx6661/article/details/52132575"
    ]

    def parse(self, response):
        pass
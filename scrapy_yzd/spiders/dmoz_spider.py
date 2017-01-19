# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_yzd.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["gamersky.com"]
    start_urls = [
        "http://www.gamersky.com/review/top/List_52.shtml",
        "http://www.gamersky.com/review/top/List_51.shtml",
        "http://www.gamersky.com/review/top/List_50.shtml",
        "http://www.gamersky.com/review/top/List_49.shtml",
        "http://www.gamersky.com/review/top/List_48.shtml"
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
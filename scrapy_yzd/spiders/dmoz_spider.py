# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_yzd.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.gamersky.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/title').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['time'] = sel.xpath('div[@class="time"]/text()').extract()
            yield item
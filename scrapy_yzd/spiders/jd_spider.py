# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import jdItem
import json

class jdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com",
                       "3.cn"]
    start_urls = [
        "https://list.jd.com/list.html?cat=9987,653,655"  # 手机
    ]

    def parse(self, response):
        for href in response.xpath('//div/@data-sku'):
            url = "https://item.jd.com/" + href.extract() + ".html"
            yield scrapy.Request(url, callback=self.parse_each_phone)

    def parse_price(self, response):
        print 'Processing price........................'
        item = response.meta['item']
        price_str = response.body
        price_str = price_str[2:-4]
        print price_str
        js = json.loads(str(price_str))
        print js
        print js['p']
        item['phone_price'] = js['p']
        yield item
        # return item

    def parse_each_phone(self, response):
        item = jdItem()
        each_id = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li[2]/@title').extract()
        item['phone_id'] = each_id
        item['phone_name'] = response.xpath('//div[@class="sku-name"]/text()').extract()
        each_id = str(each_id[0])
        print 'Processing phone:................' + each_id + '..........................'
        url = "https://p.3.cn/prices/mgets?callback=&skuIds=J_" + each_id
        print url
        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_price)
        # yield item







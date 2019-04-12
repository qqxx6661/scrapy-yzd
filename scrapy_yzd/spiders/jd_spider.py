# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import jdItem
import json
import time


class jdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com",
                       "3.cn"]
    start_urls = [
        "http://list.jd.com/list.html?cat=9987,653,655&page=1&delivery=1&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main"
    ]

    def parse(self, response):
        a = 0
        for href in response.xpath('//div/@data-sku'):
            url = "https://item.jd.com/" + href.extract() + ".html"
            print url
            yield scrapy.Request(url, callback=self.parse_each_phone)
            a += 1
        print "This page's phone number:" + str(a)

        time.sleep(20)
        next_page = response.xpath('//a[@class="pn-next"]/@href').extract()
        if next_page:
            next_page = "https://list.jd.com" + next_page[0]
            print '--------------Finding next page--------------------------', next_page
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            print '--------------There is no more page!--------------------------'

    def parse_price(self, response):
        item = response.meta['item']
        price_str = response.body
        price_str = price_str[2:-4]
        js = json.loads(str(price_str))
        print js['p']
        item['phone_price'] = js['p']
        yield item
        # return item

    def parse_each_phone(self, response):
        item = jdItem()
        each_id = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li[2]/@title').extract()
        item['phone_id'] = each_id
        item['phone_name'] = response.xpath('normalize-space(//div[@class="sku-name"]/text())').extract() #到了美国有空格了，不知道为何，已修复
        item['phone_houdu'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[2]/dl/dd[4]/text()').extract()
        item['phone_CPU'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[4]/dl/dd[1]/text()').extract()
        item['phone_ROM'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[6]/dl/dd[1]/text()').extract()
        item['phone_RAM'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[6]/dl/dd[2]/text()').extract()
        item['phone_screen'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[7]/dl/dd[2]/text()').extract()
        item['phone_frontcam'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[8]/dl/dd[1]/text()').extract()
        item['phone_backcam'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[9]/dl/dd[2]/text()').extract()
        each_id = str(each_id[0])
        url = "https://p.3.cn/prices/mgets?callback=&skuIds=J_" + each_id
        yield scrapy.Request(url, meta={'item': item}, callback=self.parse_price)
        # yield item # 导致重复商品且无价格，原因未知
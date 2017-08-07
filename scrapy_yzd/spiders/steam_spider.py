# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import SteamItem

class steamSpider(scrapy.Spider):
    name = "steam"
    allowed_domains = ["store.steampowered.com"]
    start_urls = [
        "http://store.steampowered.com/search/"
    ]

    def parse(self, response):
        # page_number = 0
        for url in response.xpath('//*[@id="search_result_container"]/div[2]/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse_each_game)
            # page_number += 1
        # print "Page number: " + str(page_number)

    def parse_each_game(self, response):
        item = SteamItem()
        item['release_date'] = response.xpath('//*[@class="release_date"]/span/text()').extract()
        item['app_name'] = response.xpath('//*[@class="apphub_AppName"]/text()').extract()
        yield item
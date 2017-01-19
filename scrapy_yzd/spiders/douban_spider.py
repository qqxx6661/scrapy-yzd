# -*- coding: utf-8 -*-
import scrapy

from scrapy_yzd.items import DoubanItem

class DdoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/subject/26683290/"
    ]

    def parse(self, response):
            item = DoubanItem()
            item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
            item['movie_director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()
            item['movie_starring'] = response.xpath('//a[@rel="v:starring"]/text()').extract()
            item['movie_category'] = response.xpath('//span[@property="v:genre"]/text()').extract()
            item['movie_time'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
            yield item
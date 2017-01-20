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
            item['movie_star'] = response.xpath('//strong[@property="v:average"]/text()').extract()
            item['movie_5score'] = response.xpath('//span[@class="rating_per"][1]/text()').extract()
            item['movie_4score'] = response.xpath('//span[@class="rating_per"][2]/text()').extract()
            item['movie_3score'] = response.xpath('//span[@class="rating_per"][3]/text()').extract()
            item['movie_2score'] = response.xpath('//span[@class="rating_per"][4]/text()').extract()
            item['movie_1score'] = response.xpath('//span[@class="rating_per"][5]/text()').extract()
            yield item
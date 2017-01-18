# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy_yzd.items import DoubanItem

class Douban(CrawlSpider):
    name = "douban"
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        # print response.body
        item = DoubanItem()
        selector = Selector(response)
        # print selector
        Movies = selector.xpath('//div[@class="info"]')
        # print Movies
        for eachMoive in Movies:
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            # 把两个名称合起来
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            print fullTitle
            print movieInfo
            print star
            print quote
# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import DoubanItem
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "https://movie.douban.com/tag/%E5%8A%A8%E7%94%BB"
    ]


    def parse(self, response):
        for href in response.xpath('//a[@class="nbg"]/@href'):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_each_movie)
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_page:
            print '--------------Finding next page: [%s] --------------------------', next_page
            yield scrapy.Request(next_page[0], callback=self.parse)
        else:
            print '--------------There is no more page!--------------------------'


    def parse_each_movie(self, response):
        item = DoubanItem()
        item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item['movie_director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()
        item['movie_writer'] = response.xpath('//span[@class="attrs"][2]/a/text()').extract()
        item['movie_starring'] = response.xpath('//a[@rel="v:starring"]/text()').extract()
        item['movie_category'] = response.xpath('//span[@property="v:genre"]/text()').extract()
        #item['movie_language'] = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[2]
        item['movie_date'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
        item['movie_time'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
        item['movie_star'] = response.xpath('//strong[@property="v:average"]/text()').extract()
        item['movie_5score'] = response.xpath('//span[@class="rating_per"][1]/text()').extract()
        item['movie_4score'] = response.xpath('//span[@class="rating_per"][2]/text()').extract()
        item['movie_3score'] = response.xpath('//span[@class="rating_per"][3]/text()').extract()
        item['movie_2score'] = response.xpath('//span[@class="rating_per"][4]/text()').extract()
        item['movie_1score'] = response.xpath('//span[@class="rating_per"][5]/text()').extract()
        item['movie_describe'] = response.xpath('//*[@id="link-report"]/span/text()').re(r'\S+')

        check_item = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[1]
        result = self.check_contain_chinese(check_item)
        if result:
            item['movie_country'] = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[1]
        else:
            item['movie_country'] = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[2]

        yield item

    def check_contain_chinese(self, check_str):
        for ch in check_str.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


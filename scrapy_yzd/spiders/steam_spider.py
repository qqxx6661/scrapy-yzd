# -*- coding: utf-8 -*-
import scrapy
from scrapy_yzd.items import SteamItem

class steamSpider(scrapy.Spider):
    name = "steam"
    allowed_domains = ["store.steampowered.com"]

    def parse(self, response):
        for page in range(1, 1347):
            url_page = 'http://store.steampowered.com/search/?sort_by=Price_ASC&page=' + str(page)
            yield scrapy.Request(url_page,
                                 callback=self.parse_each_page)

    def parse_each_page(self, response):
        for url_game in response.xpath('//*[@id="search_result_container"]/div[2]/a/@href').extract():
            yield scrapy.Request(url_game,
                                 callback=self.parse_each_game,
                                 cookies={'mature_content': '1'})

    def parse_each_game(self, response):
        item = SteamItem()

        app_name = response.xpath('//*[@class="apphub_AppName"]/text()').extract_first()
        if app_name == '' or app_name:
            self.log('no get data meta:%s' % response.meta)
            return
        item['name'] = app_name

        price = response.xpath('//div[@class="game_purchase_price price"]/text()').extract_first()
        try:
            p = price.split('¥')
            price = int(p[1])
        except:
            price = -1
        item['price'] = price

        release_date = response.xpath('//*[@class="release_date"]/span/text()').extract_first()
        item['release_date'] = release_date

        metacritic_score = response.xpath('//div[@class="score high"]/text()').extract_first()
        try:
            metacritic_score = int(metacritic_score)
        except:
            metacritic_score = -1
        item['metacritic_score'] = metacritic_score

        # 所有用户回复数量
        user_reviews_count = response.xpath('//label[@for="review_type_all"]/span/text()').extract_first()
        user_reviews_count = self.count_to_int(user_reviews_count)
        item['user_reviews_count'] = user_reviews_count

        # 好评的用户数量
        positive_user_reviews_count = response.xpath('//label[@for="review_type_positive"]/span/text()').extract_first()
        positive_user_reviews_count = self.count_to_int(positive_user_reviews_count)
        item['positive_user_reviews_count'] = positive_user_reviews_count

        # 好评的百分比
        if user_reviews_count != -1 and positive_user_reviews_count != -1:
            positive_percent = positive_user_reviews_count * 1.0 / user_reviews_count * 100
        else:
            positive_percent = 0
        item['positive_percent'] = positive_percent

        # 差评的用户数量
        negative_user_reviews_count = response.xpath('//label[@for="review_type_negative"]/span/text()').extract_first()
        negative_user_reviews_count = self.count_to_int(negative_user_reviews_count)
        item['negative_user_reviews_count'] = negative_user_reviews_count

        # 在 steam 购买的用户的评论数
        steam_user_reviews_count = response.xpath('//label[@for="purchase_type_steam"]/span/text()').extract_first()
        steam_user_reviews_count = self.count_to_int(steam_user_reviews_count)
        item['steam_user_reviews_count'] = steam_user_reviews_count

        # 在其他平台购买的用户的评论数
        non_steam_user_reviews_count = response.xpath('//label[@for="purchase_type_non_steam"]/span/text()').extract_first()
        non_steam_user_reviews_count = self.count_to_int(non_steam_user_reviews_count)
        item['non_steam_user_reviews_count'] = non_steam_user_reviews_count

        # 英语评论的数量
        english_user_reviews_count = response.xpath('//label[@for="review_language_mine"]/span/text()').extract_first()
        english_user_reviews_count = self.count_to_int(english_user_reviews_count)
        item['english_user_reviews_count'] = english_user_reviews_count

        # 非英语的评论数量
        non_english_user_reviews_count = user_reviews_count - english_user_reviews_count
        item['non_english_user_reviews_count'] = non_english_user_reviews_count

        yield item

    def count_to_int(self, data):  # 评价数逗号括号去除
        try:
            ret = data
            ret = ret.replace('(', '')
            ret = ret.replace(')', '')
            ret = ret.replace(',', '')

            return int(ret)
        except:
            return -1

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyYzdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_director = scrapy.Field()
    movie_writer = scrapy.Field()
    movie_starring = scrapy.Field()
    movie_category = scrapy.Field()
    movie_country = scrapy.Field()
    #movie_language = scrapy.Field()
    movie_date = scrapy.Field()
    movie_time = scrapy.Field()
    movie_star = scrapy.Field()
    movie_5score = scrapy.Field()
    movie_4score = scrapy.Field()
    movie_3score = scrapy.Field()
    movie_2score = scrapy.Field()
    movie_1score = scrapy.Field()
    movie_describe = scrapy.Field()
    pass


class jdItem(scrapy.Item):
    phone_id = scrapy.Field()
    phone_name = scrapy.Field()
    phone_price = scrapy.Field()
    phone_houdu = scrapy.Field()
    phone_CPU = scrapy.Field()
    phone_ROM = scrapy.Field()
    phone_RAM = scrapy.Field()
    phone_screen = scrapy.Field()
    phone_frontcam = scrapy.Field()
    phone_backcam = scrapy.Field()
    pass

class SteamItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    release_date = scrapy.Field()
    metacritic_score = scrapy.Field()
    user_reviews_count = scrapy.Field()
    positive_user_reviews_count = scrapy.Field()
    positive_percent = scrapy.Field()
    negative_user_reviews_count = scrapy.Field()
    steam_user_reviews_count = scrapy.Field()
    non_steam_user_reviews_count = scrapy.Field()
    english_user_reviews_count = scrapy.Field()
    non_english_user_reviews_count = scrapy.Field()
    pass

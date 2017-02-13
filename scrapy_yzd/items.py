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
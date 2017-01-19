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


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    pass


class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_director = scrapy.Field()
    movie_starring = scrapy.Field()
    movie_category = scrapy.Field()
    movie_time = scrapy.Field()
    pass
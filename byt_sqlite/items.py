#!usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BytSzjjItem(scrapy.Item):
    title = scrapy.Field()
    publish = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
    pass

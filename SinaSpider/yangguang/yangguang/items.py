# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    handle_status = scrapy.Field()
    name = scrapy.Field()
    last_update = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()



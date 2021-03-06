# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BricksetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    
    name = scrapy.Field()
    pieces = scrapy.Field()
    image = scrapy.Field()
    minifigs = scrapy.Field()

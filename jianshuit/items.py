# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class JianshuitItem(Item):
    user = Field()
    time = Field()
    title = Field()
    view = Field()
    comment  = Field()
    like = Field()
    gain = Field()

    # define the fields for your item here like:
    # name = scrapy.Field()

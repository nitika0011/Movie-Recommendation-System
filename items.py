# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy.item


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
def serialize_price(value):
    return f'${str(value)}'

class Bookitem(scrapy.Item):
    url=scrapy.Field()
    title=scrapy.Field()
    upc=scrapy.Field()
    product_type=scrapy.Field()
    price_excl_tax=scrapy.Field()
    price_incl_tax=scrapy.Field()
    tax=scrapy.Field()
    Availability=scrapy.Field()
    No_of_reviews=scrapy.Field()
    star=scrapy.Field()
    category=scrapy.Field()
    description=scrapy.Field()
    price=scrapy.Field()
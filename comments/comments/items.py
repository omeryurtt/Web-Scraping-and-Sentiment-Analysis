# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CommentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    asin = scrapy.Field()
    user_name = scrapy.Field()
    review_star = scrapy.Field()
    review_title = scrapy.Field()
    text = scrapy.Field()
    date_and_country = scrapy.Field()
    product_name = scrapy.Field()
    pass

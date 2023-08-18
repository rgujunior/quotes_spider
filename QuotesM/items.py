import scrapy


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()

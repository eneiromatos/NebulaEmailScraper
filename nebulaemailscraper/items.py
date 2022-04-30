import scrapy
from itemloaders.processors import TakeFirst


class EmailItem(scrapy.Item):
    url = scrapy.Field()
    emails = scrapy.Field()


class ProjectDetailsItem(scrapy.Item):
    scraped_at = scrapy.Field()

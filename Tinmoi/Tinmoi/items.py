# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TinmoiItem(scrapy.Item):

    Tieu_de = scrapy.Field()
    Ngay = scrapy.Field()
    Noi_dung_chinh = scrapy.Field()
    Tac_gia = scrapy.Field()
    pass

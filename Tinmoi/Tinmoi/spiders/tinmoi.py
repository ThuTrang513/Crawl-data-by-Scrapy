import scrapy
from Tinmoi.items import TinmoiItem

class TinmoiSpider(scrapy.Spider):
    name = 'tinmoi'
    allowed_domains = ['tinmoi.vn']
    start_urls = ['http://tinmoi.vn/']
    def parse(self, response):
        for i in range (1,865):
            base_urls = 'https://tinmoi.vn/kinh-doanh/page/'
            yield scrapy.Request(url = base_urls + str(i),callback = self.parselink)
    def parselink(self,response):
        for article in response.css("div.flex-one-mb"):
            link = article.css("a::attr(href)").get()
            yield scrapy.Request(url = link,callback = self.parse_product) 
    def parse_product(self, response):
        article = TinmoiItem()
        article['Tac_gia'] = response.css("div.footer-content strong::text").get()
        article['Tieu_de'] = response.css('div.title-page-detail > h1::text').get() 
        article['Ngay'] = response.css('div.title-page-detail span::text').get()
        article['Noi_dung_chinh'] = response.css('div.title-page-detail > h2::text').get()
        yield article

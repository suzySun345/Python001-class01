import scrapy


class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanspider'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ['http://https://maoyan.com//']

    def parse(self, response):
        pass

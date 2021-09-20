import scrapy


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['www.federica.eu/tutti-i-mooc']
    start_urls = ['http://www.federica.eu/tutti-i-mooc/']

    def parse(self, response):
        pass

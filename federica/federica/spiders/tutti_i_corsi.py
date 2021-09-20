import scrapy
from .models import Course


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['federica.eu']
    start_urls = ['http://www.federica.eu/tutti-i-mooc/']

    def parse_details(self, response):
        description_div = response.xpath(
            '//div[./*[contains(text(), "Descrizione")]]')
        yield {
            'description': ' '.join(description_div.css('p::text, strong::text').getall())
        }

    def parse_base_info(self, response):
        for course in response.css('div.mooc-main-box')[0:5]:
            out = Course()

            titolo_box = course.css('div.titolo-box')
            link = titolo_box.css('a')
            if link:
                out.title = link.css('::text').get()
                out.link = link.attrib['href']
            else:
                out.title = titolo_box.css('::text').get()
                out.link = None

            out.area = course.xpath(
                'div/div[contains(@class, \'area-segmento\')]/text()').get()
            out.status = course.css('div.info-card2 div::text').get()
            out.teacher = course.css('div.docente-box::text').get()
            out.short_description = course.css('p.abstract-box::text').get()

            yield out.__dict__

    def parse(self, response):
        yield from self.parse_base_info(response)

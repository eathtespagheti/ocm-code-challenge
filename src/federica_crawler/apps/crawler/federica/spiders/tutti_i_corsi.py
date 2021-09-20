import scrapy
from .models import Course


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['federica.eu']
    url = 'http://www.federica.eu/tutti-i-mooc'

    def parse_details(self, response, course: Course):
        if self.lang == 'it':
            description_div = response.xpath(
                '//div[./*[contains(text(), "Descrizione")]]')
        elif self.lang == 'en':
            description_div = response.xpath(
                '//div[./*[contains(text(), "Description")]]')

        course.description = ' '.join(
            description_div.css('p::text, strong::text').getall())
        return course.__dict__

    def parse_base_info(self, response):
        for course in response.css('div.mooc-main-box'):
            out = Course()

            titolo_box = course.css('div.titolo-box')
            link = titolo_box.css('a')
            if link:
                out.title = link.css('::text').get()
                out.link = response.urljoin(link.attrib['href'])
                details_request = scrapy.Request(
                    out.link+self.lang_parameter, self.parse_details, cb_kwargs=dict(course=out))
            else:
                out.title = titolo_box.css('::text').get()
                out.link = None

            out.area = course.xpath(
                'div/div[contains(@class, \'area-segmento\')]/text()').get()
            out.status = course.css('div.info-card2 div::text').get()
            out.teacher = course.css('div.docente-box::text').get()
            out.short_description = course.css('p.abstract-box::text').get()

            if self.deep:
                yield details_request
            else:
                yield out.__dict__

    def start_requests(self):
        self.lang = getattr(self, 'lang', 'it')
        self.lang_parameter = '&lang=' + self.lang
        self.deep = getattr(self, 'deep', '')
        if self.deep == 'True':
            self.deep = True
        if self.lang == 'en':
            self.url = 'http://www.federica.eu/' + self.lang + '/all-moocs'
        yield scrapy.Request(self.url, self.parse_base_info)
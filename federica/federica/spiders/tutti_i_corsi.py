import scrapy


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['www.federica.eu/tutti-i-mooc']
    start_urls = ['http://www.federica.eu/tutti-i-mooc/']

    def parse(self, response):
        for course in response.css('div.mooc-main-box'):
            titolo_box = course.css('div.titolo-box')
            link = titolo_box.css('a')
            if link:
                title = link.css('::text').get()
                link = link.attrib['href']
            else:
                title = titolo_box.css('::text').get()
                link = None
            yield {
                'title': title,
                'link': link,
                'status': course.css('div.info-card2 div::text').get(),
                'teacher': course.css('div.docente-box::text').get()
            }

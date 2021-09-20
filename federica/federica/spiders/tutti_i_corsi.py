import scrapy


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['federica.eu']
    start_urls = ['http://www.federica.eu/tutti-i-mooc/']

    def parse_base_info(self, response):
        for course in response.css('div.mooc-main-box')[0:5]:
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
                'area': course.xpath('div/div[contains(@class, \'area-segmento\')]/text()').get(),
                'status': course.css('div.info-card2 div::text').get(),
                'teacher': course.css('div.docente-box::text').get(),
                'short_description': course.css('p.abstract-box::text').get()
            }

    def parse(self, response):
        yield from self.parse_base_info(response)

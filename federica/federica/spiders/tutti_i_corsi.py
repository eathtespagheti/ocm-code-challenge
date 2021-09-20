import scrapy


class TuttiICorsiSpider(scrapy.Spider):
    name = 'tutti_i_corsi'
    allowed_domains = ['www.federica.eu/tutti-i-mooc']
    start_urls = ['http://www.federica.eu/tutti-i-mooc/']

    def parse(self, response):
        for course in response.css('div.mooc-main-box div.titolo-box'):
            link = course.css('a')
            if link:
                title = link.css('::text').get()
                link = link.attrib['href']
            else:
                title = course.css('::text').get()
                link = None
            yield {
                'title': title,
                'link': link
            }

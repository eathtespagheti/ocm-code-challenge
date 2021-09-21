#!/usr/bin/env python3
from scrapy.crawler import CrawlerRunner
from apps.crawler.spiders.corsi import CorsiSpider
from apps.crawler.settings import settings
from twisted.internet import reactor


def collect_data():
    """Collect data using CorsiSpider and load it in the db"""

    runner = CrawlerRunner(settings=settings)
    runner.crawl(CorsiSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


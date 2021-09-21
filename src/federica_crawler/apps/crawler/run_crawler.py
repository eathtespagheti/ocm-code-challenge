#!/usr/bin/env python3
from scrapy.crawler import CrawlerProcess
from apps.crawler.spiders.corsi import CorsiSpider
from apps.crawler.settings import settings

process = CrawlerProcess(settings=settings)

process.crawl(CorsiSpider)
process.start()  # the script will block here until the crawling is finished

#!/usr/bin/env python3
from scrapy.crawler import CrawlerRunner
from apps.crawler.spiders.corsi import CorsiSpider
from apps.crawler.settings import settings
from twisted.internet import reactor
from multiprocessing import Process, Queue

# stolen from https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable
def run_spider(spider, *args, **kwargs):
    def f(q):
        try:
            runner = CrawlerRunner(settings=settings)
            deferred = runner.crawl(spider, args=args, kwargs=kwargs)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result


def collect_data(*args, **kwargs):
    """Collect data using CorsiSpider and load it in the db"""

    run_spider(CorsiSpider, args=args, kwargs=kwargs)
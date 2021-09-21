settings = {
    # Scrapy settings for federica project
    #
    # For simplicity, this file contains only settings considered important or
    # commonly used. You can find more settings consulting the documentation:
    #
    #     https://docs.scrapy.org/en/latest/topics/settings.html
    #     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
    #     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

    'BOT_NAME': 'federica',

    'SPIDER_MODULES': ['apps.crawler.spiders'],
    'NEWSPIDER_MODULE': 'apps.crawler.spiders',


    # Crawl responsibly by identifying yourself (and your website) on the user-agent
    #USER_AGENT = 'federica (+http://www.yourdomain.com)'

    # Obey robots.txt rules
    'ROBOTSTXT_OBEY': True,

    # Configure item pipelines
    # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    'ITEM_PIPELINES': {
        'apps.crawler.pipelines.TitlePipeline': 300,
        'apps.crawler.pipelines.NotNullPipeline': 301,
        'apps.crawler.pipelines.StripWhitespacesPipeline': 302,
        'apps.crawler.pipelines.SaveItemPipeline': 303,
    },
}

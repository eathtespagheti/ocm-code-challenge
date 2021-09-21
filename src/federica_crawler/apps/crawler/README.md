# Scrapy for federica.eu website

Scrapy projects for scraping courses from [Federica](https://www.federica.eu) website

## How to run

Since this scrapy project it's strictly integrated with django model it require to run from a python shell or script where django has already been loaded.

A quick way to get a django ready python shell it's to run `django-admin shell` or `python manage.py shell` and from there

```python
from apps.crawler.run_crawler import collect_data
collect_data()
```

`collect_data` supports keyworded arguments that allow the usage of spiders arguments

## Arguments

There are two arguments for the `CorsiSpider` spider:
* lang: could be either `it` or `en`, default to `it`: Select the italian or english page for federica.eu
* deep: `True` or anything else, default `False`: Set this to true to scrape every single course page, this will populate the `description` field and not only the `short_description` from the main page. Using this option may require a lot of time for the scraper to complete (and probably will get your IP banned because of too many requests)


## Pipelines

All scraped data it's manipulated via 4 pipelines and then finally saved in the django webapp database

* `TitlePipeline`: Discard all items missing a title parameter
* `NotNullPipeline`: Check all text based field for null values and replace them with blank strings
* `StripWhitespacesPipeline`: Remove both leading and trailing whitespaces/tabs/newlines from strings
* `SaveItemPipeline`: Manage all the saving tasks for the various models, avoids duplicates and find data for ForeignKeys in the database

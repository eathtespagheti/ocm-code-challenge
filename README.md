# Code Challenge for [ofcourseme](https://ofcourse.me/)

It's all written using python apps, mainly [scrapy](https://scrapy.org) as scraper and [Django](https://www.djangoproject.com) for managing and displaying the data

All the web app it's containerized with docker

For further informations I've written three separated readmes:

* [Django](src/federica_crawler/README.md)
* [Scrapy](src/federica_crawler/apps/crawler/README.md)
* [Docker](stack/README.md)

## Notes

Some features don't work, one of them it's using [scrapy args](src/federica_crawler/apps/crawler/README.md#arguments) from within the django webforms, it's a django related issue since they work fine from commandline

As I've mentioned in the [Django README](src/federica_crawler/README.md#course), teachers should be a ManyToMany field, but I didn't had enough time to implement that
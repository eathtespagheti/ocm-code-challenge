# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from apps.crawler.models import Course
from scrapy_djangoitem import DjangoItem

class CourseItem(DjangoItem):
    django_model = Course

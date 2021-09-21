# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from apps.courses.models import Course
from scrapy_djangoitem import DjangoItem

class CourseItem(DjangoItem):
    """Mirror between Course model from django and a Scrapy Item"""
    django_model = Course

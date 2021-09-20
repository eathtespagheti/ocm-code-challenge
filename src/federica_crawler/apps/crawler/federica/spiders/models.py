from apps.crawler.models import Course
from scrapy_djangoitem import DjangoItem

class CourseItem(DjangoItem):
    django_model = Course
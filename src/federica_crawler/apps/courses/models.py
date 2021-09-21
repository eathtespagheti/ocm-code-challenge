from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True, default='')
    area = models.CharField(max_length=200, blank=True, default='')
    status = models.CharField(max_length=200, blank=True, default='')
    teacher = models.CharField(max_length=200, blank=True, default='')
    short_description = models.CharField(max_length=300, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')

    def __str__(self) -> str:
        return self.title
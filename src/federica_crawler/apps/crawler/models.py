from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    area = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(null=True)
    area = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    teacher = models.CharField(max_length=200, null=True)
    short_description = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.title
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Status(models.Model):
    """This model represent a Course Status"""

    value = models.CharField(max_length=50, blank=True,
                             default='', unique=True)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse("Status_detail", kwargs={"pk": self.pk})


class Course(models.Model):
    """This model represent a single Course"""

    title = models.CharField(max_length=200, unique=True)
    url = models.URLField(blank=True, default='')
    area = models.CharField(max_length=200, blank=True, default='')
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    teacher = models.CharField(max_length=200, blank=True, default='')
    short_description = models.CharField(
        max_length=300, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

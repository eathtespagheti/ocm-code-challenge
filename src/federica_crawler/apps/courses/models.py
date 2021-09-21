from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Status(models.Model):
    """This model represent a Course Status"""

    value = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse("Status_detail", kwargs={"pk": self.pk})


class Area(models.Model):
    """This model represent a Course area"""
    value = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse("area_detail", kwargs={"pk": self.pk})


class Teacher(models.Model):
    """This model represent a Course teacher"""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"pk": self.pk})


class Course(models.Model):
    """This model represent a single Course"""

    title = models.CharField(max_length=200)
    url = models.URLField(blank=True, default='')
    area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(
        'Teacher', on_delete=models.SET_NULL, null=True)
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

from django.test import TestCase
from .models import Status, Area, Teacher

class StatusTestCase(TestCase):
    def setUp(self):
        Status.objects.create(value="test")

    def test_has_value(self):
        """Taste value field and __str__"""
        s = Status.objects.get(value="test")
        self.assertEqual(s.__str__(), 'test')

class AreaTestCase(TestCase):
    def setUp(self):
        Area.objects.create(value="test")

    def test_has_value(self):
        """Taste value field and __str__"""
        s = Area.objects.get(value="test")
        self.assertEqual(s.__str__(), 'test')

class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(name="test")

    def test_has_name(self):
        """Taste name field and __str__"""
        s = Teacher.objects.get(name="test")
        self.assertEqual(s.__str__(), 'test')
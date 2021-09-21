from django.test import TestCase
from .models import Status, Area, Teacher, Course


class StatusTestCase(TestCase):
    '''Test Status model'''

    def setUp(self):
        Status.objects.create(value="test")

    def test_has_value(self):
        """Taste value field and __str__"""
        s = Status.objects.get(value="test")
        self.assertEqual(s.__str__(), 'test')


class AreaTestCase(TestCase):
    '''Test Area model'''

    def setUp(self):
        Area.objects.create(value="test")

    def test_has_value(self):
        """Taste value field and __str__"""
        s = Area.objects.get(value="test")
        self.assertEqual(s.__str__(), 'test')


class TeacherTestCase(TestCase):
    '''Test Teacher model'''

    def setUp(self):
        Teacher.objects.create(name="test")

    def test_has_name(self):
        """Taste name field and __str__"""
        s = Teacher.objects.get(name="test")
        self.assertEqual(s.__str__(), 'test')


class CourseTestCase(TestCase):
    '''Test Course model'''

    def setUp(self):
        Course.objects.create(title="test")

    def test_has_title(self):
        """Taste title field and __str__"""
        s = Course.objects.get(title="test")
        self.assertEqual(s.__str__(), 'test')

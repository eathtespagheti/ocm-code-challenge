from django.test import TestCase
from .models import Status, Area, Teacher, Course
from .views import ButtonActions
from django.test.client import RequestFactory


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


class TestButtonActionsView(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_init(self):
        request = self.factory.get('/button_actions/?scrape=Scrape+new+data')
        response = ButtonActions(request)
        self.assertEqual(response.template_name, 'courses/actions/scrape.html')
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/button_actions/?delete=Delete+Courses')
        response = ButtonActions(request)
        self.assertEqual(response.template_name, 'courses/actions/delete.html')
        self.assertEqual(response.status_code, 200)
        
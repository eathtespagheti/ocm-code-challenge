from django.test import TestCase
from apps.crawler.pipelines import StripWhitespacesPipeline, CourseItem, NotNullPipeline


class NotNullPipelineTestCase(TestCase):
    '''Test NotNullPipeline pipeline'''

    def test_not_null(self):
        """Taste for null fields replaced by ''"""
        c = CourseItem(title='test', url=' a', status=' stat  ')
        pipeline = NotNullPipeline()
        c = pipeline.process_item(c, None)

        self.assertEqual(c['area'], '')
        self.assertEqual(c['teacher'], '')
        self.assertEqual(c['short_description'], '')
        self.assertEqual(c['description'], '')


class StripWhiteSpacesPipelineTestCase(TestCase):
    '''Test StripWhiteSpacesPipeline pipeline'''

    def test_has_value(self):
        """Taste value field and __str__"""
        c = CourseItem(title='test', url=' a', status=' stat  ')

        # Clean null values
        pipeline = NotNullPipeline()
        c = pipeline.process_item(c, None)

        pipeline = StripWhitespacesPipeline()
        c = pipeline.process_item(c, None)

        self.assertEqual(c['title'], 'test')
        self.assertEqual(c['url'], 'a')
        self.assertEqual(c['status'], 'stat')

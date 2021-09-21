# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import typing
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from apps.crawler.items import CourseItem
from apps.courses.models import Status, Teacher, Area, Course


class TitlePipeline:
    """Pipeline that ensure every item has a title"""

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if item has a title field, in case it's blank or None drop the Item"""
        adapter = ItemAdapter(item)
        if not adapter.get('title'):
            raise DropItem(f"Missing title in {item}")

        return item


class NotNullPipeline:
    """Pipline that ensure every None textbased field it's replaced by blank"""

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Set None fields to a blank string

        Work on the following fields:
        url,
        area,
        status,
        teacher,
        short_description,
        description
        """

        adapter = ItemAdapter(item)

        if not adapter.get('url'):
            adapter['url'] = ''
        if not adapter.get('area'):
            adapter['area'] = ''
        if not adapter.get('status'):
            adapter['status'] = ''
        if not adapter.get('teacher'):
            adapter['teacher'] = ''
        if not adapter.get('short_description'):
            adapter['short_description'] = ''
        if not adapter.get('description'):
            adapter['description'] = ''

        return item


class StripWhitespacesPipeline:
    """Remove excess whitespaces from fields"""

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check and remove leading and trailing whitespaces from strings"""

        adapter = ItemAdapter(item)

        adapter['title'] = str(adapter['title']).strip()
        adapter['url'] = str(adapter['url']).strip()
        adapter['area'] = str(adapter['area']).strip()
        adapter['status'] = str(adapter['status']).strip()
        adapter['teacher'] = str(adapter['teacher']).strip()
        adapter['short_description'] = str(
            adapter['short_description']).strip()
        adapter['description'] = str(adapter['description']).strip()

        return item


class SaveItemPipeline:
    """Pipeline that ensure there are no duplicates and saves Item to database"""

    def get_area(self, item: CourseItem) -> typing.Union[Area, None]:
        """Check if area it's already saved in db, then return the right area instance for the item"""
        adapter = ItemAdapter(item)
        if adapter.get('area'):
            return Area.objects.get_or_create(value=adapter.get('area'))[0]
        else:
            return None

    def get_status(self, item: CourseItem) -> typing.Union[Status, None]:
        """Check if status it's already saved in db, then return the right status instance for the item"""
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            return Status.objects.get_or_create(value=adapter.get('status'))[0]
        else:
            return None

    def get_teacher(self, item: CourseItem) -> typing.Union[Teacher, None]:
        """Check if teacher it's already saved in db, then return the right teacher instance for the item"""
        adapter = ItemAdapter(item)
        if adapter.get('teacher'):
            return Teacher.objects.get_or_create(name=adapter.get('teacher'))[0]
        else:
            return None

    def check_duplicate(self, item: CourseItem):
        """Check if two scraped Courses with the same title have also the same url

        If they have both title and url equal Drop the item
        """
        same_title = CourseItem.django_model.objects.filter(
            title=item['title'])
        if same_title and Course(same_title.first()).url == item['url']:
            raise DropItem(
                f"Duplicated course title and url for {item['title'], item['url']}")
        return item

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if Item it's already present in database, if not saves it"""
        self.check_duplicate(item)

        item['area'] = self.get_area(item)
        item['status'] = self.get_status(item)
        item['teacher'] = self.get_teacher(item)
        item.save()
        return item

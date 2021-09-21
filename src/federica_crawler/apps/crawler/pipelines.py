# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import typing
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from apps.crawler.items import CourseItem
from apps.courses.models import Status


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


class SaveItemPipeline:
    """Pipeline that ensure there are no duplicates and saves Item to database"""

    def get_status(self, item: CourseItem) -> typing.Union[Status, None]:
        """Check if status it's already saved in db, then return the right status instance for the item"""
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            return Status.objects.get_or_create(value=adapter.get('status'))[0]
        else:
            return None

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if Item it's already present in database, if not saves it"""
        if CourseItem.django_model.objects.filter(title=item['title']):
            raise DropItem(f"Duplicated course title for {item['title']}")

        item['status'] = self.get_status(item)
        item.save()
        return item

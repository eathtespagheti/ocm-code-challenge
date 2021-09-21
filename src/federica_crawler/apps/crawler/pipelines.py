# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from apps.crawler.items import CourseItem


class TitlePipeline:
    """Pipeline that ensure every item has a title"""

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if item has a title field, in case it's blank or None drop the Item"""
        adapter = ItemAdapter(item)
        if not adapter.get('title'):
            raise DropItem(f"Missing title in {item}")
        else:
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

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if Item it's already present in database, if not saves it"""
        if CourseItem.django_model.objects.filter(title=item['title']):
            raise DropItem(f"Duplicated course title for {item['title']}")
        else:
            item.save()
            return item

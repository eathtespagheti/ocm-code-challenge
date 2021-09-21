# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from apps.crawler.federica.items import CourseItem


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
        if adapter.get('url') == None:
            adapter['url'] = ''
        if adapter.get('area') == None:
            adapter['area'] = ''
        if adapter.get('status') == None:
            adapter['status'] = ''
        if adapter.get('teacher') == None:
            adapter['teacher'] = ''
        if adapter.get('short_description') == None:
            adapter['short_description'] = ''
        if adapter.get('description') == None:
            adapter['description'] = ''

        return item


class SaveItemPipeline:
    """Pipeline that ensure there are no duplicates and saves Item to database"""

    def process_item(self, item: CourseItem, spider) -> CourseItem:
        """Check if Item it's already present in database, if not saves it"""
        item.save()
        return item

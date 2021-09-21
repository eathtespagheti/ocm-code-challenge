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

    def process_item(self, item: CourseItem, spider):
        """Check if item has a title field, in case it's blank or None drop the Item"""
        adapter = ItemAdapter(item)
        if not adapter.get('title'):
            raise DropItem(f"Missing title in {item}")
        item.save()
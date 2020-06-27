# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        i_type = item['m_type']
        i_time = item['m_time']
        output = f'{name}\t{i_type}\t{i_time}\n'
        with open('./scrapy_result.csv', 'a+', encoding="utf-8") as result:
            result.write(output)
        return item

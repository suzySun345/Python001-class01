# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
dbInfo = {
        'host': '60.205.205.219',
        'port': '3306',
        'user': 'root',
        'password': '345513',
        'db': 'db01'

    }
class IpproxyPipeline:
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        name = adapter['name']
        i_type = adapter['m_type']
        i_time = adapter['m_time']
        # output = f'{name}\t{i_type}\t{i_time}\n'
        # with open('./scrapy_result.csv', 'a+', encoding="utf-8") as result:
        #     result.write(output)

        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
        )
        cur = conn.cursor()
        try:
            output = [name, i_type, i_time]
            cur.execute('Insert into scrapy values(%s,%s,%s)', output)
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        finally:
            conn.close()

        return item

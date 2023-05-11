# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
from itemadapter import ItemAdapter


class PostgresPipeline:
    def __init__(self, postgres_uri):
        self.postgres_uri = postgres_uri

    @classmethod
    def from_crawler(cls, crawler):
        postgres_uri = crawler.settings.get('POSTGRES_URI')
        return cls(postgres_uri)

    def open_spider(self, spider):
        self.connection = psycopg2.connect(self.postgres_uri)

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        cursor = self.connection.cursor()
        query = """
            INSERT INTO results (url_part, title, img)
            VALUES (%s, %s, %s)
        """
        values = (item['url_part'], item['title'], item['img'])
        cursor.execute(query, values)
        self.connection.commit()
        return item




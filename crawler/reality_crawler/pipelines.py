# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time

import psycopg2
from itemadapter import ItemAdapter
from psycopg2 import sql


class PostgresPipeline:
    def __init__(self, postgres_uri):
        time.sleep(20)
        self.postgres_uri = postgres_uri
        self.connection = psycopg2.connect(self.postgres_uri[:-8])

    @classmethod
    def from_crawler(cls, crawler):
        postgres_uri = crawler.settings.get('POSTGRES_URI')
        return cls(postgres_uri)

    def open_spider(self, spider):

        # cursor = self.connection.cursor()
        self.connection.autocommit = True  # !
        #
        # create_cmd = sql.SQL('CREATE DATABASE sreality;')
        # cursor.execute(create_cmd)
        # cursor.close()
        # self.connection.close()

        self.connection = psycopg2.connect(self.postgres_uri)
        cursor = self.connection.cursor()
        query = """
        
        DROP TABLE IF EXISTS results;
        
        CREATE TABLE results (
             url_part TEXT,
            title TEXT,
           img TEXT
        );
        """
        cursor.execute(query)

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




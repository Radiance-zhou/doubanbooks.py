# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
from scrapy.conf import settings


class MongoDBPipeline(object):
    def __init__(self):
        host = settings['MONGODB_SERVER']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DB']
        client = MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item

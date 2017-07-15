# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    """
    去重

    一个用于去重的过滤器，丢弃那些已经被处理过的item。
    让我们假设我们的item有一个唯一的ori_pic_url，但是我们spider返回的多个item中包含有相同的ori_pic_url
    """

    def __init__(self):
        self.ori_pic_urls_seen = set()

    def process_item(self, item, spider):
        if item['ori_pic_url'] in self.ori_pic_urls_seen:
            raise DropItem("Duplicate item found: {}".format(item))
        else:
            self.ori_pic_urls_seen.add(item['ori_pic_url'])
            return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        # 多进程设置 connect=False
        self.client = pymongo.MongoClient(self.mongo_uri, connect=False)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__
        # 直接插入数据库
        # self.db[collection_name].insert(dict(item))
        # 先验证数据库，没有则添加数据
        self.db[collection_name].update({'ori_pic_url': item['ori_pic_url']}, {'$set': item}, True)
        return item

    def close_spider(self, spider):
        self.client.close()

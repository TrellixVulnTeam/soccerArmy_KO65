# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GoodspyPipeline(object):
    def process_item(self, item, spider):
        print("Process Item")
        return item

    def open_spider(self, spider):
        print("Abriu o Spider")

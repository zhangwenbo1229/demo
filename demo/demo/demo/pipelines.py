# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
class DemoPipeline(object):
    def open_spider(self,spider):
        self.mysql_con = pymysql.connect('localhost', 'zwb', '123456', 'bqb',autocommit=True)
        self.cur = self.mysql_con.cursor()

    def process_item(self, item, spider):
        for i in range(len(item['image_url'])):
            query = 'INSERT  INTO bqb_scrapy(`image_url`,`image_des`) values("{}","{}");'.format(item['image_url'][i],item['image_des'][i])
            self.cur.execute(query)
        return item


    def close_spider(self, spider):
        self.mysql_con.close()
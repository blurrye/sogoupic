# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SogoupicItem(scrapy.Item):
    title = scrapy.Field()
    tags = scrapy.Field()
    # 原始图片所在网页
    page_url = scrapy.Field()
    # 原图-source
    ori_pic_url = scrapy.Field()
    # 原图-sogoucdn
    pic_url = scrapy.Field()
    # 图片大小，宽
    width = scrapy.Field()
    # 图片大小，高
    height = scrapy.Field()
    # 图片大小，字节
    size = scrapy.Field()

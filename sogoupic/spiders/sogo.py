# -*- coding: utf-8 -*-
import scrapy
from urllib.request import quote
import json
from sogoupic.items import SogoupicItem
from sogoupic.settings import *


class SogoSpider(scrapy.Spider):
    name = 'sogo'
    allowed_domains = ['pic.sogou.com']
    url_template = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category={category}&tag={tag}&start={start}&len=15'

    # 网址规律很明显,Ajax,json
    # start_urls = [
    #     'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%A5%B3%E7%A5%9E&start=0&len=15',
    #     'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%A5%B3%E7%A5%9E&start=15&len=15',
    #     'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%A5%B3%E7%A5%9E&start=30&len=15',
    # ]
    # ### 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=美女               &tag=女神             &start=45&len=15'

    def start_requests(self):
        category = quote(CATEGORY)
        tag = quote(TAG)
        for start in range(START, END + 1):
            url_next = self.url_template.format(category=category, tag=tag, start=start * 15)
            print(url_next)
            yield scrapy.Request(url_next, callback=self.parse)

    def parse(self, response):
        results = json.loads(response.text)
        item = SogoupicItem()
        if 'all_items' in results.keys():
            # 每页15幅图片
            for result in results.get('all_items'):
                for field in item.fields:
                    if field in result.keys():
                        item[field] = result.get(field)
                # item存1幅图片信息
                yield item

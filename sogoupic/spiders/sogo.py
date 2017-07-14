# -*- coding: utf-8 -*-
import scrapy


class SogoSpider(scrapy.Spider):
    name = 'sogo'
    allowed_domains = ['pic.sogou.com']
    start_urls = ['http://pic.sogou.com/']

    def parse(self, response):
        print(response.text)

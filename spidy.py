# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpidySpider(CrawlSpider):
    name = 'spidy'
    allowed_domains = ['http://www.abacusconsultants.org/']
    start_urls = ['http://http://www.abacusconsultants.org//']

    rules = (
        Rule(LinkExtractor(allow='/index/'), follow=True),
        Rule(LinkExtractor(allow='/view/'), callback='parse_item')
)

    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

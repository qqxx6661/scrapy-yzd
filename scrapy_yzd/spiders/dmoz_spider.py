import scrapy
from scrapy.selector import Selector
from scrapy_yzd.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[normalize-space(@class)="title-and-desc"]')
        items = []

        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)
        return items

import hashlib
import os
import htmlmin
import scrapy

try:
    from ..items import CrawlerItem
except Exception: #ImportError
    from crawler.crawler.items import CrawlerItem


class SiteSpider(scrapy.Spider):
    name = "site"
    # allowed_domains = ["www.w3schools.com"]
    # start_urls = ["http://www.w3schools.com/xml/"]
    # allowed_domains = ["https://www.zalando.ch/"]
    # start_urls = ["https://www.zalando.ch/herren-accessoires"]
    allowed_domains = ["http://www.sme.sk"]

    # return iteration of requests which the spider will crawl from
    def start_requests(self):
        urls = ["http://sport.sme.sk",
                "http://m.smedata.sk/api-media"
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        file_name = self.hash_url(response.url)
        page = response.url.split("/")[-2]
        file_name_html = 'site-%s.html' % page
        directory = 'testdir'

        # if the directory does not exists, build one
        if not os.path.exists(directory):
            os.makedirs(directory)

        # fill the directory with a file of scraped content
        with open(directory + '/' + file_name, 'wb') as f:
            content = htmlmin.minify(response.body.decode('utf-8'))
            f.write(bytes(content, 'utf-8'))

        with open(directory + '/' + file_name_html, 'wb') as f2:
            f2.write(response.body)

        for anchor in response.xpath('//a'):
            item = CrawlerItem()
            item['title'] = anchor.xpath('text()').extract()
            item['link'] = anchor.xpath('@href').extract()
            item['image'] = anchor.xpath('img').extract()
            self.get_children(item)

    def hash_url(self, url):
        return hashlib.md5(url.encode('utf-8')).hexdigest()

    def get_children(self, item):
        print(item)
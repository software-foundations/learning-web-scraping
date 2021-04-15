import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    allowed_domains = ['https://www.coursera.org/browse?language=pt']
    start_urls = ['http://https://www.coursera.org/browse?language=pt/']

    def parse(self, response):
        self.log('Hello world from project!')

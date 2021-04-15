import scrapy


class GilenoFilhoSpider(scrapy.Spider):
	name = 'gilenofilho'
	start_urls = ['http://www.gilenofilho.com.br']

	def parse(self, response):
		self.log('Hello World')
		self.log(response.body)

# scrapy runspider 02_scrapy_intro.py
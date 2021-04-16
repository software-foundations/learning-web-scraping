import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    allowed_domains = ['https://www.udacity.com/courses/all']
    start_urls = ['http://https://www.udacity.com/courses/all/']

    def parse(self, response):        
        courses = response.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/main/div[2]/ul/li')        
        for course in courses:
            title = course.xpath('.//h2').xpath('.//text()').extract_first()
            link = course.xpath('.//a/@href').extract_first()
            img = course.xpath('.//a/article/div[1]/div/@style').extract_first().split(',')[-1].replace(')', '')
            description = course.xpath('.//a/article/div[2]/div[1]/p/text()').extract_first()
            yield {
                'title': title,
                'url': link,
                'image': img,
                'description': description
            }

import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    allowed_domains = ['https://www.udacity.com']
    start_urls = ['http://https://www.udacity.com/courses/all']

    def parse(self, response):
        # courses = response.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/main/div[2]/ul/li')
        courses = response.xpath('//ul[contains(@class, "catalog-card-list_catalogCardList__3RHuK")]/li')
        for course in courses:            
            link = course.xpath('.//a')
            href = link.xpath('.//@href').extract_first()            
            
            yield scrapy.Resques(
                url=f"https://www.udacity.com{href}",
                calllback=self.parse_detail
            )

    def parse_detail(self, response):
        title = response.xpath('.//h2').xpath('.//text()').extract_first()        
        description = response.xpath('.//div[contains(@class, "contentful-hero_legible__ktvso center hidden-xs-down")]/text()').extract_first()        
        image = response.xpath('.//div[contains(@class, "contentful-hero_heroBg__2rSX2")]/@style').extract_first().split('//')[1].replace(')', '')
        # instructors = list(map(
        #     lambda x: x.xpath('.//h5/text()').extract_first(), 
        #     response.xpath('//a[contains(@class, "degree-instructors_card__2gugh border-card_card__1pCLA")]')))

        instructors = []
        for a in response.xpath('//a[contains(@class, "degree-instructors_card__2gugh border-card_card__1pCLA")]'):
            instructors.append(
                {
                    'name': a.xpath('.//h5/text()').extract_first(),
                    'image': a.xpath('.//img/@src').extract_first().split(',')[1]
                }
            )

        yield {
            'title': title,
            'description': description,
            'image': image,
            'instructors': instructors
        }

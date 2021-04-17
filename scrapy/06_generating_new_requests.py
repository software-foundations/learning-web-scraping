title = response.xpath('//title/text()').extract_first()

subtittle = response.xpath('//div[contains(@class, "hidden-xs-down")]/text()').extract_first()

response.xpath('//a[contains(@class, "degree-instructors_card__2gugh border-card_card__1pCLA")]')

instructors = list(map(
	lambda x: x.xpath('.//h5/text()').extract_first(), 
	response.xpath('//a[contains(@class, "degree-instructors_card__2gugh border-card_card__1pCLA"): ]')))
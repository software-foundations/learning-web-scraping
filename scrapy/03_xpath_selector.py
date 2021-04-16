response

div = response.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/main/div[2]/ul/li[3]/a/article')

div.extract()

divs_courses = response.xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/main/div[2]/ul/li')

for n, div_course in enumerate(divs_courses):
	h2 = div_course.xpath('.//a/article/div[2]/div[1]/h2')
	print(h2.extract_first())
	if n == 10:
		break

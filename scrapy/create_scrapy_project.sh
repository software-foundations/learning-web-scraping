# create a project
scrapy startproject courses

# create a spyder
cd courses
scrapy genspider coursera https://www.coursera.org/browse\?language\=pt

# run a spyder
scrapy crawl coursera
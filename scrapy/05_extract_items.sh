# Create the spyder "udacity" hosted in "courses" project
scrapy genspider udacity https://www.udacity.com/courses/all

# open page in terminal
scrapy shell https://www.udacity.com/courses/all

# execute spyder
scrapy crawl udacity

# execute spyder and save output in a json
scrapy crawl udacity -o udacity_courses.json

# execute spyder and save output in a csv
scrapy crawl udacity -o udacity_courses.csv
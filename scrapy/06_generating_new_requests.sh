cd courses

# request the url for the course itself
scrapy shell https://www.udacity.com/course/data-engineer-nanodegree--nd027

# run the udacity spyder and save the output in a json
scrapy crawl udacity -o udacity_courses.json
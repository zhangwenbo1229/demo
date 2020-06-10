import scrapy

class demo(scrapy.Spider):
    name = 'doutula'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/photo/list/']
    for i in range(2,19):
        start_urls.append("https://www.doutula.com/photo/list/?page={}".format(i))

    def parse(self, response):
        item = {}
        item['image_url'] = response.css("div.random_picture").css("a>img::attr(data-original)").extract()
        item['image_des'] = response.css("div.random_picture").css("a>p::text").extract()
        yield item
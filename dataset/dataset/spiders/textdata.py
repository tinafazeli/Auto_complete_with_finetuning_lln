import scrapy


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["www.mehrnews.com"]
    start_urls = ["https://www.mehrnews.com"]

    def parse(self, response):
        for paragrapgh in response.css('p'):
            yield{
                'text': paragrapgh.get()
            }

        for href in response.css('a::attr(href)'):
            yield response.follow(href,self.parse)

# class FullSite(scrapy.Spider):
#     name="full"
#     allowed_domains = ["www.mehrnews.com"]
#     start_urls = ["https://www.mehrnews.com"]
#     def parse(self, response):
#         for paragrapgh in response.css('p'):
#             yield{
#                 'text': paragrapgh.get()
#             }
#         for heading in response.css('h1,h2,h3,h5,h6'):
#             yield{
#                 'text':heading.get()
#             }
#         for link in response.css('a::atrr(href)').getall():
#           if link:
#               yield response.follow(link,self.parse)  

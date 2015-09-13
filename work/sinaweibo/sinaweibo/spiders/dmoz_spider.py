
#import scrapy
#
#class DmozSpider(scrapy.spiders.Spider):
#    name = "dmoz"
#    allowed_domains = ["dmoz.org"]
#    start_urls = [
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#    ]
#    
#    def parse(self, response):
#        filename = response.url.splite("/")[-2]
#        with open(filename, 'wb') as f:
#            f.write(response.body)



#    ################################################### 

#       
#from scrapy.spider import BaseSpider
#
#class DmozSpider(BaseSpider):
#    name = "dmoz"
#    allowed_domains = ["dmoz.org"]
#    start_urls = [
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#    ]
#
#    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        open(filename, 'wb').write(response.body)


#    ################################################### 

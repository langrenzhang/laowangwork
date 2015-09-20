
import scrapy

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"
    ]
       
    def parse(self, response):
        
        for sel in response.xpath('//ul/'):
            
            item = DmozItem()
            item['title'] = sel.xpath('li/text()').extract()
            item['link'] = sel.xpath('li/@href').extract()
#            item['desc'] = sel.xpath('text()').extract()
            yield item
    
   
        
        
            
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

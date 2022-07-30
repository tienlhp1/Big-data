import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
file = open('24h.csv', 'w',newline="", encoding='utf8')
fields = ["headline","description","content","datepublish","cate"]
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()
class MySpider(CrawlSpider):
   name = '24h'
   start_urls = ['https://www.24h.com.vn/']

   rules = (Rule(LinkExtractor(allow=(r'\.html$')),callback='parse_item',follow=True),)

   def parse_item(self, response):

       #vexpress
       self.logger.info('Hi, this is an item page! %s', response.url)
       headline = response.xpath("//h1[@class='clrTit bld tuht_show']/text()").get()
       if headline is not None: 
            headline = headline.rstrip().strip()
       print("/////////////////////",headline)
       des = response.xpath("//h2[@class='ctTp tuht_show']/text()").get()
       if (des is None):
           des = response.css("h2.tuht_show >strong::text").get()
       if des is not None: 
            des = des.rstrip().strip()
       print("/////////////////////",des)
       content = response.xpath("//p/text()").getall()
       if content is not None:
           content = " ".join(content)
       print("/////////////////////",content)
       date =  response.xpath("//time[@class='cate-24h-foot-arti-deta-cre-post']/text()").get()
       if (date is None):
            date = response.xpath("//div[@class='updTm updTmD mrT5']/text()").get()
       if date is not None:
            date = date.split(",")[1]
            date = date.split(" ")[2]
       print("/////////////////////",date)
       cate = response.css("ul.brm >li >a.brmItem >span::text").get()     
       if (cate is None):
           cate = response.css("ul.d-flex >li >a.active::text").get()
       if cate is not None: 
            cate = cate.rstrip().strip()
       print("/////////////////////",cate)
       if (headline is not None) and (des is not None) and (content is not None) and (date is not None) and (cate is not None):
           writer.writerow({"headline": headline, "description": des, "content": content, "datepublish": date,"cate":cate})
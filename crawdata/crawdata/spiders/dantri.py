import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
file = open('dantri.csv', 'w',newline="", encoding='utf8')
fields = ["headline","description","content","datepublish","cate"]
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()
class MySpider(CrawlSpider):
   name = 'dantri'
   allowed_domains = ["dantri.com.vn"]
   start_urls = ['https://dantri.com.vn/']

   rules = (Rule(LinkExtractor(allow=(r'\.htm$')),callback='parse_item',follow=True),)

   def parse_item(self, response):

       #vexpress
       self.logger.info('Hi, this is an item page! %s', response.url)
       headline = response.xpath("//h1[@class='title-page detail']/text()").get()
       if headline is not None: 
            headline = headline.rstrip().strip()
       print("/////////////////////",headline)
       des = response.xpath("//h2[@class='singular-sapo']/text()").get()
       if des is not None: 
            des = des.rstrip().strip()
       print("/////////////////////",headline)
       content = response.xpath("//p/text()").getall()
       if content is not None:
           content = " ".join(content)
       print("/////////////////////",content)
       date = response.css("time.author-time::text").get()
       
       if date is not None:
            date = date.split(",")[1]
            date = date.split(" ")[1]
       if date is not None: 
            date = date.rstrip().strip()
       print("/////////////////////",date)
       cate = response.css("ul.breadcrumbs >li >a::text").get() 
       print("/////////////////////",cate)
       if (headline is not None) and (des is not None) and (content is not None) and (date is not None) and (cate is not None):
           writer.writerow({"headline": headline, "description": des, "content": content, "datepublish": date,"cate":cate})
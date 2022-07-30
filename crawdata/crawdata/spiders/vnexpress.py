import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
file = open('vnexpress.csv', 'w',newline="", encoding='utf8')
fields = ["headline","description","content","datepublish","cate"]
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()
class MySpider(CrawlSpider):
   name = 'vnexpress'
   allowed_domains = ["vnexpress.net"]
   start_urls = ['https://vnexpress.net/']

   rules = (Rule(LinkExtractor(allow=(r'\.html$')),callback='parse_item',follow=True),)

   def parse_item(self, response):

       #vexpress
       self.logger.info('Hi, this is an item page! %s', response.url)
       headline = response.css("h1.title-detail::text").get()
       if headline is not None: 
            headline = headline.rstrip().strip()
       print("/////////////////////",headline)
       des = response.css("p.description::text").get()
       if des is not None: 
            des = des.rstrip().strip()
       print("/////////////////////",des)
       content = response.css("p.Normal::text").getall()
       if content is not None:
           content = " ".join(content)
       print("/////////////////////",content)
       date = response.css("span.date::text").get()
       
       if date is not None:
            date = date.split(",")[1]
       if date is not None: 
            date = date.rstrip().strip()
       print("/////////////////////",date)
       cate = response.css("ul.breadcrumb >li >a::text").get()
       if cate is not None: 
            cate = cate.rstrip().strip()
       print("/////////////////////",cate)
       if (headline is not None) and (des is not None) and (content is not None) and (date is not None) and (cate is not None):
           writer.writerow({"headline": headline, "description": des, "content": content, "datepublish": date,"cate":cate})
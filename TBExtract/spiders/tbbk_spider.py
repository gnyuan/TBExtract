#/usr/bin/python
#-*-coding:utf-8-*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log
import json

from TBExtract.items import TBExtractItem

url = "https://shopsearch.taobao.com/search?app=shopsearch&initiative_id=staobaoz_20120515&q=abc"

class TBSpider(Spider):

    name = "TBSpider"
    download_delay = 4
    allowed_domains = ["taobao.com"]
    start_urls = [
        url
        ]

    def parse(self, response):
        sel = Selector(response)
 
        shops = sel.xpath("//script/text()").re("\s*g\_page\_config\s=\s(.*);")[0]
        print "*************response url:%s******************" %response.url

        shops = json.loads(shops)
        shops = shops['mods']['shoplist']['data']['shopItems']

        for shop in shops:
            item = TBExtractItem()
            print "*************shop in shops******************"
            item['nick'] = shop['nick'].encode('UTF-8')
            item['uid'] = shop['uid'].encode('UTF-8')
            item['title'] = shop['title'].encode('UTF-8')
            item['shopUrl'] = shop['shopUrl'].encode('UTF-8')

            yield item

        for pagenum in range(20,201,20):
            print "URL = " + url+"&s="+str(pagenum)
            yield Request(url+"&s="+str(pagenum), callback=self.parse)    

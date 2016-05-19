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
    # start_urls = [
    #     url
    #     ]
    start_urls = [ url+'&s='+str(pagenum) for pagenum in range(0, 401, 20) ]

    def parse(self, response):
        sel = Selector(response)
 
        shops = sel.xpath("//script/text()").re("\s*g\_page\_config\s=\s(.*);")[0]
        print "*************response url:%s******************" %response.url

        shops = json.loads(shops)
        shops = shops['mods']['shoplist']['data']['shopItems']

        for shop in shops:
            item = TBExtractItem()
            item['nick'] = shop['nick'].encode('UTF-8')
            item['uid'] = shop['uid'].encode('UTF-8')
            item['title'] = shop['title'].encode('UTF-8')
            item['shopUrl'] = shop['shopUrl'].encode('UTF-8')
            item['setupdate'] = 'xxxxx'
            # yield item
            request = Request('https:'+ item['shopUrl'], callback=self.parse_shop)
            request.meta['item'] = item 
            yield request

    def parse_shop(self, response):
        print "*************response url:%s******************" %response.url
        # nick = response.xpath('//a[@class="shop-name"]/span/text()').extract.endcode('UTF-8')
        item = response.meta['item']
        item['setupdate'] = response.xpath('//span[@class="id-time"]/text()').extract()[0].encode('UTF-8')
        return item
        # print 'setupdate = ' + item['setupdate']
        # return item

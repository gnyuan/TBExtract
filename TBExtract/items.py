#-*-coding:utf-8-*-

from scrapy.item import Item, Field

class TBExtractItem(Item):
    """存储条目信息"""

    nick = Field()
    uid = Field()
    title = Field()
    shopUrl = Field()
    setupdate = Field()


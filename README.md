TBExtract
============

这个项目主要用来抓取淘宝的数据。分为以下几个步骤

###数据选择
抓取商铺信息，例如[这个入口](https://shopsearch.taobao.com/search?app=shopsearch&initiative_id=staobaoz_20120515&q=abc&s=0),从里面提取店铺的名称、ID、昵称等。

###XPATH分析
使用Chrome、XPATHhelper等工具获得所要提取目标的位置。(这时最关键的一步，分析目标值所在位置)

###提取内容
用Scrapy的流程来提取目标值。

###使用方法
scrapy crawl TBSpider

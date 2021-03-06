# Scrapy settings for TBExtract project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'TBExtract'

SPIDER_MODULES = ['TBExtract.spiders']
NEWSPIDER_MODULE = 'TBExtract.spiders'

ITEM_PIPELINES = {
    'TBExtract.pipelines.TBExtractPipeline':300
}

COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'TBExtract (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
     'TBExtract.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
}
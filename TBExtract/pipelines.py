import json
import codecs

class TBExtractPipeline(object):
    def __init__(self):
        self.file = codecs.open("taobao_data.json", encoding="utf-8", mode="wb")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

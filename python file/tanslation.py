from urllib import request as r
from urllib import parse as p
import json
import time

content = input("pls enter the words (enter 'wq' to quit query): ")
while True:
    if content == 'wq':
        break;
    else:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        # define headers NOTICE: this is a DICTIONARY
        data = dict()
        data["i"] = content
        data['from'] = "AUTO"
        data["to"] = "AUTO"
        data["smartresult"] = "dict"
        data["client"] = "fanyideskweb"
        data["salt"] = "1541145732981"
        data["sign"] = "ca94536ea9198da549863c032ab2a7f9"
        data["doctype"] = "json"
        data["version"] = "2.1"
        data["keyfrom"] = "fanyi.web"
        data["action"] = "FY_BY_REALTIME"
        data["typoResult"] = "false"  # urlencode是将数据变为同意识别的url的格式
        data = p.urlencode(data).encode('utf-8')  # 如果不加encode 这个类型为string类型 但是Request里要求data 类型为byte
        req = r.Request(url, data, headers)  # this is adding headers
        url_open = r.urlopen(req)
        # print(type(url_open))
        # url_open=r.urlopen(url,data)
        url_read = url_open.read().decode('utf-8')  # 如果不用decode 则输出会用utf-8的形式
        # 并且此类型的 byte type if decode type is string
        # automatically be utf-8 if without decode
        # print(url_read)
        # print(type(url_read))

        text = json.loads(url_read)
        #print(text)
        # print(type(text))
        if text['translateResult'][0][0]['tgt'] == content:
            print("Check speaking, there is may have a spell mistake.")
        else:
            print("Translation is: {}".format(text['translateResult'][0][0]['tgt']))
        time.sleep(1.5)
        content = input("pls enter another words (enter 'wq' to quit query): ")



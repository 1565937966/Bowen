
from urllib import request as r
import re
from bs4 import BeautifulSoup as bs
open_url=r.Request("http://baike.baidu.com/view/284853.htm")
html=r.urlopen(open_url)
html=html.read().decode('utf-8')


html_soup=bs(html,'html.parser')

a = html_soup.find_all(href=re.compile('view'))

for each in a:#不能直接print(a.text)因为a.text是一个迭代对象所以要用循环来进行输出
    #print(each.name+''.join(["http://baike.baidu.com"+each["href"]]))
    print(each.name)



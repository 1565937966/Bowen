from urllib import request
from bs4 import BeautifulSoup as bs
import re
import time

pages = int(input("Pls enter the number of pages you wanna get from the google: "))
pages = pages*10
html_holder = []
counter = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
main_path = "https://www.google.com/search?q=fintech+syllabus&ei=NUSwXO_LAdXO0PEPk_C22A0&start="
for index in range(0, pages, 10):
    url = main_path + str(index)
    get_request = request.Request(url, headers=headers)
    get_response = request.urlopen(get_request)
    '''
    html = get_response.read()
    html_holder.append(html)
    print("%d web stored" % counter)
    counter += 1
    time.sleep(10)
    '''
    soup = bs(get_response, "html.parser")
    edu_html = soup.find_all(href=re.compile(".edu"))
    for each_edu in edu_html:
        html_holder.append(each_edu["href"])
for number in range(0, len(html_holder)):
    print(html_holder[number]+"\n")
    counter += 1
    print("-------------------------------------------")
print("total %d .edu web" % counter)




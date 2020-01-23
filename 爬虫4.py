from typing import Dict

from bs4 import BeautifulSoup as bf
from urllib import request as req
import re

Original_URL = "http://classes.bus.oregonstate.edu/ba371/reitsma/research_productivity/"
Html_holder = []
Get_request = req.Request(Original_URL)
response = req.urlopen(Get_request)
html = response.read().decode("utf-8")
print(response.headers)
'''
html_soup = bf(html, "html.parser")
Authors = html_soup.findAll(href=re.compile("/ba371/reitsma/research_productivity/"))
for every_author in Authors:
    Html_hodler.append("http://classes.bus.oregonstate.edu" + every_author["href"])
for every_html in Html_hodler:
    print(every_html)
    '''

''''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
url = "https://movie.douban.com/chart"
req = request.Request(url, headers=headers)
html = request.urlopen(req)
html_soup = bf(html, "html.parser")
Movies = html_soup.find_all('a')  # href=re.compile("https://movie.douban.com/subject/")
for every_movie in Movies:
    if every_movie.get("title") is not None:
        print(every_movie.get("title") + " :")
        print(every_movie.get("href"))
        Information[str(every_movie.get("title"))] = str(every_movie.get("href"))
Actors = html_soup.find_all('p', {'class': 'pl'})
for actor in Actors:
    actor = str(actor).split('<p class="pl">')
    print(actor[1])

Url_Finance = "https://finance.yahoo.com/quote/BAC/history?p=BAC"
Req = request.Request(Url_Finance, headers=headers)
Html = request.urlopen(Req)
Finance_Soup = bf(Html, 'html.parser')
print(Finance_Soup.prettify())
'''
string = "The rain in Spain"
target = re.search("^The.*Spain$", string)
if target:
    print("Inside")
else:
    print("Outside")
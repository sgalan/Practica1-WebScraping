import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import time

# load table
df = pd.read_csv('TED_CN_2018.csv', low_memory=False)
# filter column by ISO_COUNTRY == ES
df_ES = df[df['ISO_COUNTRY_CODE']=='ES']
# keep unique URL
unique_url = df_ES.drop_duplicates(subset=['TED_NOTICE_URL'])

header_dict = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9,ca;q=0.8,en;q=0.7,nl;q=0.6",
    "Host": "httpbin.org",
    "Referer": "https://www.scraperapi.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5f93b147-070a862577ae5966438af607"}

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:3000]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

proxies = get_proxies()
proxy_pool = cycle(proxies)

with open('/Users/sgalan/Documents/UOC/Tipologia_cicle_vida/nuts_codeES.csv','w+') as w:
    for index, row in unique_url.iterrows():
        html = 'http://'+str(row['TED_NOTICE_URL'])
        proxy = next(proxy_pool)
        try:
            page = requests.get(html, proxies={"http":proxy, "https":proxy}, headers=header_dict)
            soup = BeautifulSoup(page.content)
            NUTSCODE = soup.find('span', class_ = 'nutsCode').contents[0].split()[0]
            w.write('{}\t{}\n'.format(html, NUTSCODE))
            print (html, NUTSCODE)
            time.sleep(12)
        except:
            print (html, "Skipping. connection error")
            time.sleep(10)
w.close()
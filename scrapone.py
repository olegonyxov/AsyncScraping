import datetime
import asyncio
import time

import bs4
import requests


with open("news_sites.txt", "r") as nfile:
    nlist =["https://www."+ a.rstrip("\n") for a in nfile.readlines()]



def get_title():
    urllist = []
    time_s= time.monotonic()
    for url in nlist:
        try:
            urltitle=[]
            print(url)
            reqs= requests.get(url)
            soup=bs4.BeautifulSoup(reqs.text,"html.parser")
            for title in soup.find_all("title"):
                urltitle.append(title.get_text())
            urllist.append([url,urltitle])
        except:
            pass
    print(time.monotonic() - time_s)
    return urllist


for a in get_title():
    print(a)


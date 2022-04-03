import asyncio
import time

import aiohttp
import bs4
import datetime
resplist=[]
with open("news_sites.txt", "r") as nfile:
    url_list =["https://www."+ a.rstrip("\n") for a in nfile.readlines()]
# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp


async def do_resp(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text_to_parse = await resp.text()
            soup = bs4.BeautifulSoup(text_to_parse, "html.parser")
            title = soup.find_all("title")
            return url,title

async def do_tasks():
    tasks=[]
    for url in url_list:
        tasks.append(asyncio .create_task(do_resp(url)))
    gather = await asyncio.gather(*tasks)
    for g in gather:
        print(g)



if __name__ == '__main__':
    stime=time.monotonic()
    asyncio.run(do_tasks())
    print(time.monotonic()-stime)




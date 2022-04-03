import asyncio
import aiohttp
import bs4
endlist = []
with open("news_sites.txt", "r") as nfile:
    url_list = ["https://www." + a.rstrip("\n") for a in nfile.readlines()]


async def work_response():
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            async with session.get(url) as resp:

                urltitle = []
                text_to_parse = await resp.text()
                soup = bs4.BeautifulSoup(text_to_parse, "html.parser")
                title = soup.find_all("title")

            print(url,title)


asyncio.run(work_response())
import datetime
import asyncio


with open("news_sites.txt", "r") as nfile:
    nlist =["https://www."+ a.rstrip("\n") for a in nfile.readlines()]



def get_1():
    for url in nlist:
        yield url


async def get_2():

    await asyncio.sleep(0)
    pass


endlist = []
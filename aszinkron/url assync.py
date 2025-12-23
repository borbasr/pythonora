from turtledemo.penrose import start
import time
import request
import aiohttp
import requests

URLS = [
    "https://python.org",
    "https://google.com",
    "https://www.httpbin.org/delay/2",
    "https://github.com"
]

async def check_url(session: aiohttp.ClientSession, url: str):
    print(f'[ASSZINKRON] lekérés indul: {url}')
    try:
        async with session.get(url) as response:
            print(f'[ASSZINKRON] {url} -> {response.status}')
    except asyncio.TimeoutError as e:
        print(f'[ASSZINKRON] TimeOut Hiba {url} -> {e}')
    except aiohttp.ClientError as e:
        print(f'[ASSZINKRON] Client Hiba {url} -> {e}')


async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in URLS:
            tasks.append(asyncio.create_task(check_url(session, url)))

        await asyncio.gather(*tasks)

    endTime = time.time()
    print(f'Össz futtatási idő (ASSZINKRON) {endTime - start:.2f} mp')

if __name__ == "__main__":
    asyncio.run(main())


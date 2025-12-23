import asyncio
import random
import time

async def work(id: int, sema: asyncio.Semaphore):
    async with sema:
        print(f'MUNKA {id} Elindult')
        await asyncio.sleep(random.uniform(a: 1, b: 5))
        print(f'MUNKA {id} Kilepett a feldolgozasbol')

async def main():
    start = time.time()
    sema = asyncio.Semaphore(3)

    tasks = [
        asyncio.create_task(work(i, sema)) for i in range(1, 21)
    ]

    await asyncio.gather(*tasks)
    end = time.time()
    print(f'Osszesen {end - start:.2f} mp')

if __name__ == '__main__':
    asyncio.run(main())

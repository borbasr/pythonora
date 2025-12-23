import asyncio
import time

async def stopper():
    start = time.time()
    while True:
        elapsed = time.time() - start
        print(f'Elapsed time: {elapsed:.1f} masodperc')
        await asyncio.sleep(1.0)

async def short_task():
    print('Rovid kis feladat')
    await asyncio.sleep(2)
    print('Rovid Feladat vege 2mp')

async def long_task():
    print('Hosszu kis feladat')
    await asyncio.sleep(9)
    print('Hosszu Feladat vege 9mp')

async def main():
    stopper_task = asyncio.create_task(stopper())
    short_t = asyncio.create_task(short_task())
    long_t = asyncio.create_task(long_task())
    await asyncio.gather(stopper_task, short_t, long_t)

    stopper_task.cancel()

asyncio.run(main())

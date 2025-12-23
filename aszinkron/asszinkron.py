import random
import time
import asyncio


async def asszinkron(n: int):   # 1 usage
    print(f'asszinkron feladat fut {n}')
    sleep_time = random.uniform(a:0, b:2)
    await asyncio.sleep(sleep_time)
    print(f'asszinkron feladat befejezodott {n} ({sleep_time: .2f} mp)')


async def main():
    start = time.time()

    tasks = []
    for i in range(1, 4):
        tasks.append(asyncio.create_task(asszinkron(i)))

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f'Ossz futtatasi ido {end_time - start: .2f} mp')


asyncio.run(main())


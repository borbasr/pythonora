import threading
import time
import asyncio


def fake_io_task(task_id: int, delay: float = 1.0):
    print(f'[SZINKRON] Task {task_id} START (thread: {threading.current_thread().name})')
    time.sleep(delay)
    print(f'[SZINKRON] Task {task_id} END (thread: {threading.current_thread().name})')


async def async_fake_io_task(task_id: int, delay: float = 1.0):
    print(f'[ASSZINKRON] Task {task_id} START (thread: {threading.current_thread().name})')
    await asyncio.sleep(delay)
    print(f'[ASSZINKRON] Task {task_id} END (thread: {threading.current_thread().name})')

def run_sync_io(num_task: int = 10):
    print('== SZINKRON DEMO ==')
    start = time.time()

    for i in range(1, num_task + 1):
        fake_io_task(i)

    total = time.time() - start
    print(f'[SZINKRON] ossz futtatasi ido: {total:.2f} mp')

async def run_async_io(num_task: int = 10):
    print('== ASSZINKRON DEMO ==')
    start = time.time()

    tasks = []
    for i in range(1, num_task + 1):
        tasks.append(asyncio.create_task(async_fake_io_task(i)))

    await asyncio.gather(*tasks)

    total = time.time() - start
    print(f'[ASSZINKRON] ossz futtatasi ido: {total:.2f} mp')

def run_threaded_io(num_task: int = 10):
    print('== THREADES DEMO ==')
    start = time.time()
    threads = []

    for i in range(1, num_task + 1):
        t = threading.Thread(target=fake_io_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = time.time() - start
    print(f'[THREADES] ossz futtatasi ido: {total:.2f} mp')

def main():
    run_sync_io()
    asyncio.run(run_async_io())
    run_threaded_io()

main()





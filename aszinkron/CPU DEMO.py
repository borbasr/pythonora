import asyncio
import os
import threading
import time
from multiprocessing import Process, freeze_support


def cpu_bound_test(taks_id: int, n: int):
    print(f'[CPU] Task {taks_id} START threading: {threading.current_thread().name}, PID: {os.getgid()}')
    s = 0
    for i in range(n):
        s += i * i
    print(f'[CPU] Task {taks_id} END threading: {threading.current_thread().name}, PID: {os.getgid()}')


def run_sync_cpu(num_tasks=4, n=30000000):
    print("=== SZINKRON VERZIO ===")
    start = time.time()
    results = []
    for i in range(1, num_tasks + 1):
        results.append(cpu_bound_test(i, n))

    total = time.time() - start
    print(f'[SZINKRON] Ossz futasi ido: {total:.2f} mp')


async def async_cpu_wrapper(task_id: int, n: int):
    return cpu_bound_test(task_id, n)


async def run_async_cpu(num_tasks=4, n=30000000):
    print("=== ASSZINKRON VERZIO ===")
    start = time.time()
    tasks = []
    for i in range(1, num_tasks + 1):
        tasks.append(asyncio.create_task(async_cpu_wrapper(i, n)))

    await asyncio.gather(*tasks)
    total = time.time() - start
    print(f'[ASSZINKRON] Ossz futasi ido: {total:.2f} mp')


def run_threaded_cpu(num_tasks=4, n=30000000):
    print("=== THREADES VERZIO ===")
    start = time.time()
    threads = []
    for i in range(1, num_tasks + 1):
        t = threading.Thread(target=cpu_bound_test, args=(i, n))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total = time.time() - start
    print(f'[THREADES] Ossz futasi ido: {total:.2f} mp')


def run_multiprocessing_cpu(num_tasks=4, n=30000000):
    print("=== MULTIPROCESSINGES VERZIO ===")
    start = time.time()

    process = []
    for i in range(1, num_tasks + 1):
        p = Process(target=cpu_bound_test, args=(i, n))
        process.append(p)
        p.start()

    for p in process:
        p.join()

    total = time.time() - start
    print(f'[MULTIPROCESS] Ossz futasi ido: {total:.2f} mp')


def main():
    run_sync_cpu()
    asyncio.run(run_async_cpu())
    run_threaded_cpu()
    run_multiprocessing_cpu()


if __name__ == '__main__':
    main()
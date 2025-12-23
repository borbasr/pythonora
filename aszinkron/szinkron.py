import random
import time


def szinkron(n: int):    # 1 usage
    print(f'Szinkron feladat fut {n}')
    sleep_time = random.uniform(a:0.5,b:2.0)
    time.sleep(sleep_time)
    print(f'Szinkron feladat befejezodott {n} ({sleep_time: .2f} mp)')


def main():
    start = time.time()

    for i in range(1, 4):
        szinkron(i)

    end_time = time.time()
    print(f'Ossz futtatasi ido {end_time - start: .2f} mp')


main()

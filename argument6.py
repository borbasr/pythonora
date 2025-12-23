import argparse

def positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError('Az érték csak pozitív egész szám lehet')
    return ivalue


def main():
    parser = argparse.ArgumentParser(
        description='Pozitív egész szám teszt'
    )

    parser.add_argument('n', type=positive_int, help='pozitív egész szám')
    args = parser.parse_args()
    print('Az elfogadott érték: ', args.n)


if __name__ == '__main__':
    main()



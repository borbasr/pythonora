import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Számok átlaga.'
    )
    parser.add_argument(
        'numbers',
        type=float,
        nargs='+',
        help='Számok listája'
    )

    args = parser.parse_args()
    avg = sum(args.numbers) / len(args.numbers)
    print('Átlag: ', avg)


if __name__ == '__main__':
    main()

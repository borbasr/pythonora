import argparse

def main():

    parser = argparse.ArgumentParser(
        description='Hőmérséklet konvertáló'
    )
    parser.add_argument(
        'value', type=float, help='Hőmérséklet érték'
    )
    parser.add_argument(
        '--scale',
        choices=['C', 'F'],
        default='C',
        help='A bemeneti érték típusa (C vagy F), alapértelmezett a C'
    )

    args = parser.parse_args()

    if args.scale == 'C':
        res = args.value * 9 / 5 + 32
        print(f'A végeredmény: {res:.2f} F')
    else:
        res = (args.value - 32) * 5 / 9
        print(f'Az eredmény: {res:.2f} C')


if __name__ == '__main__':
    main()

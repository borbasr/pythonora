import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Két szám összeadása."
    )

    parser.add_argument("a", type=float, help='Az első szám')
    parser.add_argument("b", type=float, help='A második szám')

    args = parser.parse_args()

    result = args.a + args.b
    print(f'Az eredmény: {result}')

if __name__ == '__main__':
    main()

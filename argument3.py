
import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description='Fájl másolása.'
    )
    parser.add_argument('source', type=Path, help='forrás fájl')
    parser.add_argument('destination', type=Path, help='cél fájl')
    parser.add_argument('-v', '--verbose', help='részletes kiírás')

    args = parser.parse_args()

    if args.verbose:
        print(f'Másolás innen: {args.source} ide: {args.destination}')

    shutil.copy2(args.source, args.destination)

    if args.verbose:
        print('Sikeres másolás')

if __name__ == '__main__':
    main()

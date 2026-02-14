from argparse import ArgumentParser
from pathlib import Path

from backup_cli.backup_config import DEFAULT_CONFIG_PATH


def build_parser():
    parser = ArgumentParser(
        description='Backup CLI - Fajlmento eszkoz'
    )

    parser.add_argument(
        '--config',
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help=f'Config file eleresi utja (alapertelmezett: {DEFAULT_CONFIG_PATH})'
    )

    parser.add_argument(
        '--source',
        type=Path,
        help='Forras konyvtar (ez felulirja a default config beallitasokat)'
    )

    parser.add_argument(
        '--target',
        type=Path,
        help='Cel konyvtar (ez felulirja a default config beallitasokat)'
    )

    parser.add_argument(
      '--ext',
        nargs='*',
       help='Kiterjesztes szurese (pl.: --ext .txt .csv .md). Ha nincs megadva, akkor a default config a mervado'
    )
    parser.add_argument(
    '--no-recursive',
        action='store_true',
        help='Ne jarja be rekurzivan az almappakat'
    )

    subparsers = parser.add_subparsers(
        dest='command',
        required=True,
        help='Elerheto parancsok'
    )

    run_parser = subparsers.add_parser(
    'run',
        help='backup futtatasa fajlok masolassa'
    )
    run_parser.set_defaults(func=cmd_run)

    list_parser = subparsers.add_parser(
    'list',
        help='Backupolando fajlok listazasa'
    )
    list_parser.set_defaults(func=cmd_list)

    return parser

def prepare(args: argparse.Namespace) -> tuple[Path, Path, List[Path]]:
    config_path: Path = args.config
    config = load_config(config_path)

    source_dir, target_dir = resolve_paths(
        config, config_path, args.source, args.target
    )

    include_ext = resolve_extensions(config, args.ext)

    resursive = not args.no_recursive

    files = list_files_to_backup(source_dir, include_ext, resursive)

    return source_dir, target_dir, files


def cmd_list(args: argparse.Namespace) -> None:
    source_dir, target_dir, files = prepare(args)

    print(f'Source: {source_dir}')
    print(f'Target: {target_dir}')
    print(f'Talalat: {len(files)} db file')
    print("Fajlok:")
    for f in files:
        print('\t', f)


def cmd_run(args: argparse.Namespace) -> None:
    source_dir, target_dir, files = prepare(args)

    print(f'Source: {source_dir}')
    print(f'Target: {target_dir}')
    print(f'{len(files)} db file lesz mentve')
    run_backup(files, source_dir, target_dir)
    print('Mentes befejezodott!')

def main():
    parser = build_parser()
    args = parser.parse_args()

    func = getattr(args, 'func', None)

    if func is None:
        parser.print_help()
        return

    func(args)


if __name__ == '__main__':
    main()





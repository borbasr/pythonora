from pathlib import Path
from typing import Optional, List

def list_files_to_backup(
    source_dir: Path,
    include_ext: Optional[List[str]],
    recursive: bool = True,
) -> List[Path]:
    if not source_dir.is_dir():
        raise ValueError('A source dir nem letezik, vagy nem mappa!')

    if include_ext:
        include_ext = [e.lower() for e in include_ext]

    if recursive:
        candidates = source_dir.rglob("*")
    else:
        candidates = source_dir.iterdir()

    results = []
    for path in candidates:
        if path.is_file():
            if path.suffix.lower() in include_ext:
                results.append(path)
            elif not include_ext:
                results.append(path)

    return results

def relative_to_source(path: Path, source_dir: Path) -> Path:
    return path.relative_to(source_dir)

def run_backup(
    files: List[Path],
    source_dir: Path,
    target_dir: Path,
):
    if not target_dir.exists():
        target_dir.mkdir()

    for src in files:
        rel = relative_to_source(src, source_dir)
        dest = target_dir / rel
        if not dest.parent.is_dir():
            dest.parent.mkdir()
        shutil.copy2(src, dest)



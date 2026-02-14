import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG_PATH = Path("backup_config.json")
ENV_TARGET = "ENV_BACKUP_TARGET"

def load_config(path: Path):
    if not path.exists():
        return {}

    with path.open(encoding="utf-8") as f:
        return json.load(f)

def resolve_paths(
    config: Dict[str, Any],
    config_path: Path,
    cli_source: Optional[Path],
    cli_target: Optional[Path]
):

    base_dir = config_path.parent

    if cli_source is not None:
        source_dir = cli_source
    else:
        cfg_source = config.get('source_dir')
        if cfg_source:
            source_dir = (base_dir / cfg_source).resolve()
        else:
            source_dir = base_dir.resolve()

    env_target = os.getenv(ENV_TARGET)

    if cli_target is not None:
        target_dir = cli_target
    elif env_target is not None:
        target_dir = (base_dir / env_target).resolve()
    else:
        cfg_target = config.get('target_dir')
        if cfg_target:
            target_dir = (base_dir / cfg_target).resolve()
        else:
            target_dir = base_dir.resolve()

    return source_dir, target_dir

def resolve_extensions(
    config: Dict[str, Any],
    cli_ext: Optional[List[str]]
) -> List[str]:
    if cli_ext:
        exts = cli_ext
    else:
        exts = config.get(key='include_ext', default=[])

    normalized = []
    for ext in exts:
        if not ext.startswith("."):
            normalized.append("." + ext)
        else:
            normalized.append(ext)

    return normalized




import io
from pathlib import Path

from ruamel.yaml import YAML
yaml = YAML(typ='safe')

CONFIG_DIR = Path('../configs')

TMP_DIR = Path('../tmp')


def show_config(path):
    config_path = CONFIG_DIR / path
    with open(config_path, 'r') as f:
        print(f.read())


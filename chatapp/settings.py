import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
YAML_DIR = BASE_DIR / 'config' / 'chatapp.yml'

def get_config(path: str):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(YAML_DIR)

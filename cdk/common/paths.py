from pathlib import Path
import os

base_root = Path(__file__).parent.parent.parent.resolve()
venv_root = os.path.join(base_root, '.venv')
api_root = os.path.join(base_root, "heimdall", "api")
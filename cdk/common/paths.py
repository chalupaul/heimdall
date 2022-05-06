from pathlib import Path
import os

base_root = Path(__file__).parent.parent.parent.resolve()
venv_root = os.path.join(base_root, ".venv")
api_root = os.path.join(base_root, "heimdall", "api")

build_root = os.path.join(base_root, "build")
layer_dir = os.path.join(build_root, "lambda_layers")
pip_target_dir = os.path.join(build_root, layer_dir, "python")

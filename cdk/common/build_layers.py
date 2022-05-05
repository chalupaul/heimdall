import os
import paths


req_path = os.path.join(paths.pip_target_dir, "requirements.txt")

def task_build_layers():

    def ez_run(*args):
        for arg in args:
            arg()
        return ""

    def check_path():
        if not os.path.exists(paths.pip_target_dir):
            os.makedirs(paths.pip_target_dir)

    def clean_req_file():
        if os.path.exists(req_path):
            os.remove(req_path)

    def idempotize():
        return ez_run(check_path, clean_req_file)
    
    def export_libs():
        return f"poetry export -o {req_path}"
    
    def install_libs():
        return f"pip install -r {req_path} --upgrade -t {paths.pip_target_dir}"
    
    return {
        "actions":[
            idempotize(),
            export_libs(),
            install_libs(),
            ez_run(clean_req_file)
        ]
    }
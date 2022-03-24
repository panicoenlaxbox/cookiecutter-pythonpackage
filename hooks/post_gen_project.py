import os
import shutil

def replace_userprofile_in_env_file():    
    path = os.path.join(os.path.realpath(os.path.curdir), ".env")
    with open(path, "rt") as f:
        content = f.read()
    content = content.replace("${USERPROFILE}", os.environ["USERPROFILE"])
    with open(path, "wt") as f:
        f.write(content)

def remove_github_if_not_needed():    
    if not "{{cookiecutter.azure_devops_pat}}":
        shutil.rmtree(os.path.join(os.path.realpath(os.path.curdir), ".github"))

def remove_dependency_injector_if_not_needed():    
    if "{{cookiecutter.dependency_injector}}" != "y":
        project_dir = os.path.join(os.path.realpath(os.path.curdir),"{{cookiecutter.project_name}}")
        os.remove(os.path.join(project_dir, "config.yml"))
        os.remove(os.path.join(project_dir, "containers.py"))
        os.remove(os.path.join(project_dir, "logging.yml"))

replace_userprofile_in_env_file()
remove_github_if_not_needed()
remove_dependency_injector_if_not_needed()

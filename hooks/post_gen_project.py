import os
import stat
import shutil
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_DIR = os.path.join(PROJECT_DIRECTORY, 'docker', 'config')

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


shutil.copyfile(
    os.path.join(DOCKER_DIR, 'python.example.env'),
    os.path.join(DOCKER_DIR, 'python.env')
)

use_decoupled_frontend = '{{cookiecutter.use_frontend}}' == 'yes'

if not use_decoupled_frontend:
    remove("frontend")
    remove("src/nextjs")

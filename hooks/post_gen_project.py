import os
import stat
import shutil
import subprocess


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_DIR = os.path.join(PROJECT_DIRECTORY, "docker", "config")
REMOVE_PATHS = []

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


use_decoupled_frontend = "{{cookiecutter.use_decoupled_frontend}}" == "yes"
use_circle_ci = "{{cookiecutter.use_circle_ci}}" == "yes"

if not use_decoupled_frontend:
    REMOVE_PATHS += ["frontend", "src/nextjs"]

if not use_circle_ci:
    REMOVE_PATHS += [".circleci", ".ciignore"]

shutil.copyfile(
    os.path.join(DOCKER_DIR, "python.example.env"),
    os.path.join(DOCKER_DIR, "python.env"),
)

for path in REMOVE_PATHS:
    remove(path)

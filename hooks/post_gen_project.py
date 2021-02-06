import os
import stat
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_DIR = os.path.join(PROJECT_DIRECTORY, "docker", "config")
TO_REMOVE = []
TO_RENAME = []

GRAPPLE_FILES = [
    "frontend/pages/_app.grapple.tsx",
    "frontend/pages/_preview.grapple.tsx",
    "frontend/pages/[...path].grapple.tsx",
]

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def rename(filepath, new_filepath):
    if os.path.isfile(filepath):
        os.rename(filepath, new_filepath)


use_decoupled_frontend = "{{cookiecutter.use_decoupled_frontend}}" == "yes"
use_grapple = "{{cookiecutter.use_grapple}}" == "yes"
use_circle_ci = "{{cookiecutter.use_circle_ci}}" == "yes"

if not use_decoupled_frontend:
    TO_REMOVE += ["frontend", "wagtail/nextjs"]
else:
    if use_grapple:
        rename("frontend/pages/_app.grapple.tsx", "frontend/pages/_app.tsx")
        for file in GRAPPLE_FILES:
            TO_RENAME.append((file, file.replace(".grapple", "")))
    else:
        TO_REMOVE += []

if not use_circle_ci:
    TO_REMOVE += [".circleci", ".ciignore"]

shutil.copyfile(
    os.path.join(DOCKER_DIR, "python.example.env"),
    os.path.join(DOCKER_DIR, "python.env"),
)

for path in TO_REMOVE:
    remove(path)

for source, target in TO_RENAME:
    remove(target)
    rename(source, target)

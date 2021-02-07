import os
import stat
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_DIR = os.path.join(PROJECT_DIRECTORY, "docker", "config")
TO_REMOVE = []
TO_RENAME = []
GRAPPLE_FILES = [
    "frontend/pages/[...path].grapple.tsx",
    "frontend/pages/_app.grapple.tsx",
    "frontend/pages/_preview.grapple.tsx",
    "frontend/pages/index.grapple.tsx",
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
    """
    In case the project does not use a decoupled frontend, no static frontend is usefuled.
    Also: no need to have the specific nextjs app.
    """
    TO_REMOVE += ["frontend", "wagtail/nextjs"]
else:
    if use_grapple:
        """
        A set of grapple-specific files has been created, with a .grapple.tsx extension.
        In case the project uses Grapple, they should be used instead of the original ones.
        """
        for file in GRAPPLE_FILES:
            TO_RENAME.append((file, file.replace(".grapple", "")))
    else:
        """
        In case the project do not make use of Grapple, let's not keep these files.
        """
        TO_REMOVE += GRAPPLE_FILES

if not use_circle_ci:
    """
    Everything circle CI related can be removed.
    """
    TO_REMOVE += [".circleci", ".ciignore"]

shutil.copyfile(
    os.path.join(DOCKER_DIR, "python.example.env"),
    os.path.join(DOCKER_DIR, "python.env"),
)


"""
Now that all non-required files have been set, let's rename or remove these.
"""
for path in TO_REMOVE:
    remove(path)

for source, target in TO_RENAME:
    remove(target)
    rename(source, target)

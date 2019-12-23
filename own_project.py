#!/usr/bin/env python3
import os
import shutil

def own_project():
    project_name = input('insert project name (with underscores) >> ')
    author = input('insert author name >> ')
    email = input('insert author email >> ')
    os.makedirs(project_name)

    with open(os.path.join(project_name, '__init__.py'), 'w') as f:
        f.write('__version__ = \'0.1.0\'\n')

    with open('pyproject.toml', 'r') as f:
        toml_contents = f.read()

    toml_contents = toml_contents.replace('{{project_name}}', project_name)
    toml_contents = toml_contents.replace('{{author}}', author)
    toml_contents = toml_contents.replace('{{email}}', email)

    os.remove('pyproject.toml')

    with open('pyproject.toml', 'w') as f:
        toml_contents = f.write(toml_contents)

    shutil.rmtree('.git')

    os.remove(__file__)

if __name__ == '__main__':
    own_project()

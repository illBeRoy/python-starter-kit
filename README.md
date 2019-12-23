![python starter kit](./logo.svg)
> template project for quickly creating python apps

- [Features](#includes)
- [Getting Started](#getting-started)
- [Tasks](#tasks)
  * [Testing](#testing)
  * [Linting](#linting)
  * [Publishing](#publishing)

## Features
* 📦 poetry for package management
* 🔬 unittest for testing
* 🦋 pylint for linting
* 📐 mypy for type checking
* 📚 taskipy for task running
* 💻 vscode configuration

## Getting Started
1. Clone this repository using the following command:
```bash
git clone https://github.com/illBeRoy/python-starter-kit.git <your_project_name>
```

2. Run the following command (make sure you have Python ^3.5 installed):
```bash
./own_project.py
```

3. Install all the requirements for your project via poetry:
```bash
poetry install
```

## Tasks
The project contains out of the box tasks for your comfort. You can see them in the `pyproject.toml` file under the tasks section.

### Testing
In order to run all test files, simply run the test task:
```bash
poetry run task test
```
This will run all python files under `tests` which begin with `test_`. If the tests finished successfully, will run linting as well.

### Linting
If you want to check your code style and run static analysis, use the following command:
```bash
poetry run task lint
```

This will run `pylint` for code style check, following by `mypy` for static type analysis.

### Publishing
If you want to not publish broken code by mistake, you can run the following task:
```bash
poetry run task publish
```

This command runs tests and linters, and only if everything passes, publishes to pypi using `poetry publish`.

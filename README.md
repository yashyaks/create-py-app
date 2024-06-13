# create_py_app

`create_py_app` is a CLI tool designed to scaffold different types of Python projects. It allows you to quickly generate boilerplate code for Supervised Learning projects, Streamlit apps, and Flask apps.

## Features

- Scaffold a Supervised Learning project
- Scaffold a Streamlit app
- Scaffold a Flask app

## Installation

You can install the `create_py_app` package via pip:

```sh
pip install create_py_app
```

## Usage

After installing, you can use the create_py_app command to scaffold a new project.

## Create a Project

To create a new project, run:

```sh
create_py_app create_project --framework [FRAMEWORK] [PROJECT_NAME]
```

- --framework or -f: The type of project to create. Options are:
1: Supervised Learning
2: Streamlit App
3: Flask App


- [PROJECT_NAME]: The name of the project directory to create.


## Examples

1. Create a supervised learning project

```sh
create_py_app create_project --framework 1 my_supervised_learning_project
```
This will create a new directory named my_supervised_learning_project with the boilerplate code for a Supervised Learning project.
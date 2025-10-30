# python-template

## Overview
Warehouse of all python project templates
1. [hello-uv](./hello-uv)
  - basic 'hello uv' python project with unit tests.
  - useful template for small and lean python projects.
  - uses uv as package manager.
  - 'smallest python building block'
2. hello-pixi TODO
3. hello-fastapi TODO

## Similar Projects
- [python-blueprint](https://github.com/johnthagen/python-blueprint)
  - this is just a single blueprint
  - nice and super detailed
- copier https://github.com/copier-org/copier
  - A library and CLI app for rendering project templates.
UV can now [generate a sample project](https://docs.astral.sh/uv/guides/projects/#creating-a-new-project)

https://github.com/rochacbruno/python-project-template?tab=readme-ov-file

github has a use template feature
https://github.com/new?template_name=python-project-template&template_owner=rochacbruno

hashtags
#python #project-template #boilerplate #cookiecutter #python-template #generator
#template #python-project-template #mkdocs

/docs dir at root
https://www.mkdocs.org/

## Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
```

https://github.com/fpgmaas/cookiecutter-uv

workflow
uv init --bare --python-pin
# `uv init` sets up the project for uv's dependency management, creating
# a minimal pyproject.toml and a .python-version file. This is where
# uv will track dependencies and can generate a uv.lock file for
# reproducible builds.
`uv add <something>`

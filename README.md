<div id="header" align="center">
    <h1 align="center">Blog Tool</h1>
    <p align="center"><i>(for lack of imagination)</i></p>
    <img src="https://img.shields.io/github/actions/workflow/status/loveduckie/blog-tool/tests.yml?label=tests">
</div>

---

A command-line Python application for managing, exporting, and publishing your blogs to multiple platforms from Markdown format. :sparkles:

Intended to be used by developers looking to centralise and publish their blog content from a "single source of truth".

## FAQ

- What is Markdown? :memo:
  - > Markdown is a lightweight markup language that you can use to add formatting elements to plaintext text documents. Created by John Gruber in 2004, Markdown is now one of the world’s most popular markup languages.
- What is Python? :snake:
  - > Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.

## Features

- Manage, export, and publish your blog posts as Markdown files, along with associated image and video assets.
- Automatically generate impression images for your blogs.
- Automatically optimise image assets before publishing.
- Upload image assets to remote sources before publishing blogs.
- Export blogs as standalone static pages.
- Publish your blogs to multiple platforms simultaneously, including self-hosted WordPress, Hashnode, and Dev.to.

## Repository

```bash
.
├── _build
│   ├── doctrees
│   └── html
│       ├── _sources
│       └── _static
├── _static
├── _templates
├── blog_tool
│   ├── cli
│   ├── data
│   │   ├── assets
│   │   ├── config
│   │   ├── headers
│   │   └── templates
│   ├── errors
│   ├── exporters
│   │   ├── decorators
│   │   └── markdown
│   ├── git
│   ├── images
│   │   ├── processors
│   │   └── uploaders
│   ├── logging
│   │   └── formatters
│   ├── markdown
│   ├── models
│   │   ├── configuration
│   │   ├── images
│   │   └── metadata
│   ├── publishers
│   └── utility
│       ├── blogs
│       ├── click
│       ├── config
│       ├── exporters
│       ├── images
│       ├── paths
│       ├── rich
│       ├── types
│       └── uploaders
├── docker
│   └── wordpress
│       └── containers
├── logs
├── scripts
└── tests
    ├── cli
    └── click
```

## Support

This sections outlines the support for third-party tooling and services.

### Platforms

Find below the number of platforms that are (currently) supported.

- **Hashnode**
  - A blogging platform for developers.
  - [https://hashnode.com/](https://hashnode.com/)
- **Dev.to**
  - A blogging platform for developers.
  - [https://dev.to/](https://dev.to/)
- **Silverstripe**
  - An extensible content management system and framework.
  - [https://silverstripe.org](https://www.silverstripe.org/)
- **WordPress**
  - A blogging and content management system.
  - **Note:** Support available for self-hosted installations.
  - [https://wordpress.org](https://www.wordpress.org/)

## Publishers

An "Uploader" is a Python type responsible for uploading a blog to a target platform after it has been rendered or rasterized. It forms part of a pipeline for rendering and ultimately publishing the blog content to the platform specified.

## Exporters

An "Exporter" is a Python type responsible for "rendering" a blog written in Markdown as another output, such as HTML or PDF.

- **PDF**
  - Render a PDF document form a Markdown source file. The rendered output is customizable with various parameters.
- **HTML**
  - Render a HTML page or collection of pages from a Markdown source file.
- **Silverstripe (HTML)**
  - Renders the Markdown source file as a HTML page, with syntax highlighting and image assets available. Supports the [silverstripe/blog](https://addons.silverstripe.org/add-ons/silverstripe/blog) module.

## Structure

This tool manages blog posts or articles by placing them into "collections". A "collection" can be considered as a series of related blog posts. They are synonymous with a book whereby a "chapter" from a book represents a single blog post or article.

### Example

Insert example here.

## Usage

This tool is installable from PyPi by running the following command.

```bash
#!/usr/bin/env bash

pip install blog-tool
```

The tool should then be usable from the command-line by running the following.

### Creating a Blog Collection

```bash
#!/usr/bin/env bash

python -m blog-tool collections create <collection name>
```

Alternatively, the same command can be expressed as the following.

```bash
#!/usr/bin/env bash

blog-tool collections create <collection name>
```

```bash
#!/usr/bin/env bash

blog-tool collections list
```

### Images

Images are automatically uploaded to image sharing websites should there be configured API keys.

### Configuration

The default configuration file is found under `blog-tool/data/config/default.ini`.

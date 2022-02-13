# IFC 4.3 Documentation server

## Introduction

The documentation server is a web application for viewing the IFC documentation.
You can view this web application live at
http://ifc43-docs.standards.buildingsmart.org/

This web application has the following features:

 - Allows the IFC documentation to be generated without the need for proprietary
   software, and work cross platform on Windows, Mac, and Linux.
 - The written documentation is now fully captured in plain text using Markdown,
   making it easy for anyone to edit the documentation without special training.
 - All written documentation changes are tracked using Git, allowing anyone to
   edit and see edit histories.
 - Using Github, anybody can make quick online "Wiki" style edits without
   bespoke software installation.
 - Documentation layout is easily customised using HTML templates and CSS styles
 - Schema changelogs are auto generated instead of relying on manual logs
 - Schema diagrams such as entity inheritance trees and concept diagrams are
   automatically generated with automatic layouting, with SVG support and
   clickable links to ensure they are searchable and always current
 - Users can generate their own interactive diagrams that can be maintained and
   checked without the need for image editing software
 - All schema entity references are automatically linked and referenced
 - All figures are automatically captioned and numbered
 - All headers and figures are anchored for sharing portions of the
   specification with anchor links
 - Using markdown and standardised templates helps ensure consistency in layout,
   typography, tables, links, notes, and references.
 - Built-in quality checking procedures during documentation generation.
 - API for quick documentation lookup or previews
 - Mobile friendly (well, we plan on it, I would hope)

## Process

There are three aspects of the IFC documentation server.

### Schema

 - **Base schema** - The schema is stored in `schemas/IFC.xml`. This is
   currently a monolithic XMI document which describes all of the IFC schema
   modeled in UML.
 - **Property set definitions** - definitions for property and quantity sets are
   stored in `reference_schemas/psd/`

UML modeling knowledge is a prerequisite for those modifying the **Base schema**
and **Property set definitions**. However, any changes to the schema must follow
the [IFC Change
Process](https://github.com/buildingSMART/IFC4.3.x-development/wiki/IFC-4.3.x-Change-Process)
to ensure that all changes are publicly reviewed, transparent to the community,
and enlist the appropriate domain experts for quality control.

As of writing, this monolithic XMI document is generated using a the
proprietary Enterprise Architect tool. However, it is planned to be broken up
into smaller datasets and revised to allow UML modeling without proprietary or
platform requirements.

### Written documentation

 - **Static pages** - documentation that does not relate to entities in the
   schema are stored in `content/`.
 - **Schema documentation** - documentation based on entities in the schema are
   stored in `docs/schemas/`. These include data types, property sets, quantity
   sets, functions, and rules.
 - **Concepts** - documentation for IFC concepts are stored in `docs/templates/`
 - **Properties** - documentation for individual properties are stored in
   `docs/properties/`
 - **Images** - images referenced in documentation may be stored in
   `docs/figures/`

No special skills are required to edit the **Written documentation**. Just a
simple text editor will do. However, any documentation that is not a minor
formatting change must also follow the [IFC Change
Process](https://github.com/buildingSMART/IFC4.3.x-development/wiki/IFC-4.3.x-Change-Process).

### Website

 - **Preprocessor** - The _Base schema_ and _Property set definitions_
   cannot be immediately accessed by the web application due to their
   complexity. This requires a preprocessing step in `code/create_resources.sh`.
   This breaks down the complex UML / XMI data into simple JSON data that the
   web application can query.
 - **Backend** - The website itself is a Python Flask application which begins
   in `server.py`. This web application renders the preprocessed _schema_ data
   with _written documentation_ using _frontend_ layouts.
 - **Frontend** - The _written documentation_ is turned into a website
   layout using templates. Templates are defined in HTML templates in
   `code/templates/`, as well as CSS, Javascript, and images in `docs/assets/`

To edit the web application features, layouting and diagram generation, and
other more complex systems, programming knowledge is required. This is either
Python for the backend code, or HTML, CSS, and Javascript knowledge for frontend
design. Making a change to this application is no different to any other change,
and must also follow the [IFC Change
Process](https://github.com/buildingSMART/IFC4.3.x-development/wiki/IFC-4.3.x-Change-Process).

## Writing markdown

Markdown is easy to get started with. Here's a [Markdown
tutorial](https://www.markdowntutorial.com/) to learn it quickly!

However, there are some conventions established for the purposes of IFC
documentation.

TODO: how to caption and reference figures, how to create inline notes and
examples.

## Diagrams

One novel feature of this documentation system is the ability to directly edit
illustrative  schema diagrams using a text-based notation. For this purpose
Graphviz is used.  The Graphviz DOT definition language is automatically
enriched with colour conventions derived from the IFC schema.

For example, the IfcWorkPlan instantiation diagram can be included and edited in
the MD files and then be visible in the related HTML page.  Below is the
Graphviz definition of this figure. The user's input overwrites the automatic
settings. This can be verified with the IfcProject node on the HTML diagram,
whose link pointing to Building Smart website replaces the link to the entity's
HTML page.

The interactive SVG diagram can be seen on the generated HTML page here
http://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcWorkPlan.htm

## Dependencies

See `Dockerfile` for more detailed dependencies.

* Flask, gunicorn: http server and API
* Graphviz, pydot: diagram layout
* solr, pysolr: search
* supervisord: process control
* Docker: container
* Python-Markdown: document conversion
* Beautifulsoup4: HTML document post processing

## Deployment

You can deploy a container running a documentation server using Docker.

```
$ cd code/
# Build a new system image called "ifcdoc"
$ docker build -t "ifcdoc" .
# Let's see the image we just created
$ docker images
REPOSITORY   TAG           IMAGE ID       CREATED          SIZE
ifcdoc       latest        df699a56028f   12 seconds ago   3GB
# Run the image we created in a new container called "ifcdoc-container", with our local port 8080 mapped to the container's port 80
$ docker run -p 8080:80 --name "ifcdoc-container" -d "ifcdoc"
# Check running Docker processes to confirm that the container is running
$ docker ps
CONTAINER ID   IMAGE    COMMAND                  CREATED          STATUS          PORTS                                   NAMES
0d4b0775cf29   ifcdoc   "/bin/sh -c 'supervi…"   12 seconds ago   Up 11 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ifcdoc-container
```

Now you can visit the containerized deployment in your browser by visiting
`http://localhost:8080`.

You can stop the Docker container as follows:

```
$ docker stop ifcdoc-container
# Check running processes (-a flag shows all processes) to ensure it has exited
$ docker ps -a
CONTAINER ID   IMAGE    COMMAND                  CREATED         STATUS                        PORTS   NAMES
0d4b0775cf29   ifcdoc   "/bin/sh -c 'supervi…"   3 minutes ago   Exited (137) 32 seconds ago           ifcdoc-container
```

Then you can start it again:

```
$ docker start ifcdoc-container
# Check running Docker processes to confirm that the container is running
$ docker ps
CONTAINER ID   IMAGE    COMMAND                  CREATED         STATUS         PORTS                                   NAMES
0d4b0775cf29   ifcdoc   "/bin/sh -c 'supervi…"   5 minutes ago   Up 3 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ifcdoc-container
```

## Development

For local development, you can do:

```
$ cd code/
$ pip install flask Beautifulsoup4 lxml Markdown gunicorn pysolr pydot tabulate hilbertcurve==1.0.5 markdown-it-py==1.1.0 deepdiff
$ ./create_resources.sh
$ FLASK_APP=server.py FLASK_ENV=development flask run
 * Serving Flask app "server.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 155-459-101
```

Then just visit `http://127.0.0.1:5000/` to view the documentation!

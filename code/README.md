IFC 4.3 Documentation server
============================

# Introduction

This folder contains the server to facilitate  a workflow for collaborative editing of the IFC Documentation. 
The Markdown documents are taken from https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs

- Enable collaborative editing by means of the Github interface
- Enable quick edits without bespoke software by means of the Github interface
- Embed a powerful syntax for generating schema diagrams with automatic layout
- Create interactive diagrams in which the entities are clickable
- Ensure typographic consistency by using the limited but powerful Markdown syntax
- Clean-up the invalid existing .html documentation files

Fully functional and consistent HTML documentation is automatically generated from the Markdown files.  
The full generated documentation can be accessed at http://ifc43-docs.standards.buildingsmart.org/

# Diagrams

One novel feature of this documentation system is the ability to directly edit
illustrative  schema diagrams using a text-based notation. For this purpose Graphviz is used. 
The Graphviz DOT definition language is automatically enriched with colour conventions derived from the IFC schema.

For example, the IfcWorkPlan instantiation diagram can be included and edited in the MD files and then be visible in the related HTML page.
Below is the Graphviz definition of this figure. The user's input overwrites the automatic settings. This can be verified with 
the IfcProject node on the HTML diagram, whose link pointing to Building Smart website replaces the link to the entity's HTML page. 

The interactive SVG diagram can be seen on the generated HTML page here
http://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcWorkPlan.htm

# Dependencies

See `Dockerfile` for more detailed dependencies.

* Flask, gunicorn: http server and API
* Graphviz, pydot: diagram layout
* solr, pysolr: search
* supervisord: process control
* Docker: container
* Python-Markdown: document conversion
* Beautifulsoup4: HTML document post processing

# Development

You can deploy a container running a documentation server using `Dockerfile`.
However, for local development, assuming you have the dependencies, you can do:

```
$ ./create_resources.sh
$ FLASK_APP=server.py FLASK_ENV=development flask run
```

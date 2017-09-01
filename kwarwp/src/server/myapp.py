#!/usr/bin/env python
from bottle import route, run, default_app, get, static_file
import os
project_server = os.getcwd()
# make sure the default templates directory is known to Bottle
templates_dir = os.path.join(project_server, '../../src')
js_dir = os.path.join(project_server, '../../')
img_dir = os.path.join(project_server, '../../image')
print(templates_dir)


@route('/')
def index():
    return static_file("kwarwp.html", root=templates_dir)  # "Hello from bottle with Python3 !"


# Static Routes
@get("<filepath:re:.*\.py>")
def css(filepath):
    return static_file(filepath, root=templates_dir)


# Static Routes
@get("/lib/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root=js_dir)


# Static Routes
@get("/lib/image/<filepath:re:.*\.(png|jpg|svg|gif)>")
def img(filepath):
    return static_file(filepath, root=img_dir)


if __name__ == "__main__":
    run(host="localhost", port=8081)
else:
    application = default_app()

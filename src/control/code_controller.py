#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SuperPython
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# SuperPython é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""Controller handles routes starting with /code.
.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
"""
from bottle import Bottle, get, static_file
from . import py_dir
from . import model_dir
from base64 import decodebytes as dcd
from model.datasource import DS
from github.GithubException import UnknownObjectException

__author__ = 'carlo'
DEFAULT_CODE = """# default
try:
    import superpython.%s.main as main
    main.main()
except:
    from browser import document, html
    document["pydiv"].html = ""
    document["pydiv"] <= html.IMG(src="/images/site_em_construcao_.jpg")
"""

appbottle = Bottle()  # create another WSGI application for this controller and resource.
# debug(True) #  uncomment for verbose error logging. Do not use in production


# Static Routes
@get("/<:path>/__init__.py")
def init_py():
    return ""


# Static Routes
@get("/<:path>/__code/_core/<filepath:re:.*\.py>")
def core_py(filepath):
    return static_file(filepath, root=py_dir)


# Static Routes
@get("/<:path>/__code/view/kwarwp/<filepath:path>")
def view_py(filepath):
    return static_file(filepath, root=py_dir+"/kwarwp")


# Static Routes
@get("/<:path>/__code/model/<filepath:path>")
def model_py(filepath):
    return static_file(filepath, root=model_dir)


# Static Routes
@get("/<:path>/__code/_spy/<module_name>/<filepath:re:.*\.py>")
def spy(module_name, filepath):
    print("spy", module_name, filepath)
    try:
        code_file = DS.get_file_contents("_spy", module_name, filepath)
        code_str = dcd(str.encode(code_file.content)).decode("utf-8")
    except UnknownObjectException as _:
        code_str = "# File not found"
    return code_str


# Static Routes
@get("/<:path>/<project_name>/__code/<module_name:re:[a-z].*>/<filepath:re:.*\.py>")
def local_spy(project_name, module_name, filepath):
    print("local_spyspy", project_name, module_name, filepath)
    try:
        code_file = DS.get_file_contents(project_name, module_name, filepath)
        code_str = dcd(str.encode(code_file.content)).decode("utf-8")
    except UnknownObjectException as _:
        code_str = "# File not found"
    return code_str

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
from bottle import Bottle, view, HTTPError, static_file
from model import database as cs
from control import py_dir
# from lib.bottle import Bottle, view, request, response, HTTPError
# from ..models import code_store as cs
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

bottle = Bottle()  # create another WSGI application for this controller and resource.
# debug(True) #  uncomment for verbose error logging. Do not use in production


# Static Routes
@bottle.get("/_spy/_core/<filepath:re:.*\.py>")
def py(filepath):
    print("py(filepath):", filepath, py_dir)
    return static_file(filepath, root=py_dir)


'''
@bottle.get('/_<a_module>')
@view('game')
def game(a_module):
    """ Return Project editor"""
    project = "uva"
    path = "superpython.%s.%s" % (project, a_module)
    print("game(module)", path)
    return dict(projeto=a_module, codename="main.py", path=path)


@bottle.get('<pypath:path>')
def handle(pypath):
    pypath = pypath.split('_spy/')[1] if "_spy" in pypath else pypath
    print('/<pypath:path>', pypath)
    # project = request.get_cookie('_spy_project_')
    code = cs.DB.load(name=pypath)
    # print('/<pypath:path>', pypath, code and code[:200])
    if code:
        return code
    if "__init__" in pypath:
        a_module = pypath.split("/")
        # module.remove("__init__.py")
        # print('/<pypath:path__init__, pypath, module, project>', pypath, module)
        if len(a_module) >= 3:
            project, a_module, path = a_module[0], a_module[1], '/'.join(a_module[1:])
            # print('/<pypath:module, cs.DB.ismember>', module, project, cs.DB.ismember(project, module))
            if cs.DB.ismember(project, a_module):
                code = cs.DB.load(name=path)
                # print('handle/<pypath:path>', path, code and code[:80])
                if code:
                    return code
                else:
                    return DEFAULT_CODE % a_module

        return "#"

    raise HTTPError(404, "No such module.")
'''
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
from bottle import Bottle, get, view
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
MENU = "Edit,/edit/edit:Save,/edit/save:Open,/edit/open:Home,/"
CSS = "solarized codemirror bulma style roboto".split()
JS = "brython brython_stdlib codemirror show-hint python-hint active-line matchbrackets python".split()

appbottle = Bottle()  # create another WSGI application for this controller and resource.
# debug(True) #  uncomment for verbose error logging. Do not use in production


@get('/game/<mod>/<name>')
@view("gamer")
def gamer(mod, name):
    return dict(
        pagetitle="SuPyGirls - {} - {}".format(mod, name), title=name,
        image="supygirls_logo.png", mod=mod,
        brython_css=CSS, brython_js=JS,
        menu=[m.split(",") for m in MENU.split(":")])

"""
        <script type="text/javascript" src="stlib/brython.js"></script>
        <script type="text/javascript" src="stlib/brython_stdlib.js"></script>
        <script src="stlib/codemirror.js" type="text/javascript"></script>
        <script src="stlib/show-hint.js" type="text/javascript"></script>
        <script src="stlib/python-hint.js" type="text/javascript"></script>
        <script src="stlib/active-line.js" type="text/javascript"></script>
        <script src="stlib/matchbrackets.js" type="text/javascript"></script>
        <script src="stlib/python.js" type="text/javascript"></script>
"""
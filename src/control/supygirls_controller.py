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

"""Controller handles routes starting with /supygirls.
.. modulerauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
"""
from bottle import get, view, post, request, default_app
from model.datasource import DS
import json
from base64 import encodebytes as ecd
from base64 import decodebytes as dcd

__author__ = 'carlo'

MENU = "Help,/site/help.html:About,/site/about.html:Home,/"
CSS = "solarized codemirror bulma style roboto".split()
JS = "brython brython_stdlib codemirror show-hint python-hint active-line matchbrackets python".split()

GIRLS = ['Roxanne', 'Stacy', 'Libby', 'Sara', 'Kellee', 'Courtney', 'Angie', 'Parisa', 'Natalia', 'Kathryn',
         'Callie', 'Lisa', 'Ruzwana', 'Naomi', 'Tracy', 'Morgan', 'Rachel', 'Soraya', 'Amanda', 'Alexa', 'Julia',
         'Sarah', 'Heather', 'Adda', 'Samantha', 'Kristen', 'Anastasia', 'Meredith', 'Danae', 'Grace']
CGIRLS = ['Ada', 'Henrietta', 'Grete', 'Gertrude', 'Betty', 'Hedy', 'Kathleen', 'Grace', 'Mary Shaw', 'Evelyn', 'Ida',
          'Mary Klawe', 'Dana', 'Jean', 'Dame', 'Joan', 'Sister Mary', 'Margaret', 'Vera', 'Margaret Hamilton', 'Erna',
          'Margaret Fox', 'Mary Lou', 'Adele', 'Karen', 'Sandra', 'Susan Nycum', 'Phyllis', 'Elizabeth', 'Irene',
          'Sophie', 'Patricia', 'Carol', 'Carla', 'Lorinda', 'Janese', 'Roberta', 'Susan Kare', 'Radia', 'Irma',
          'Monica', 'Eva', 'Frances Allen', 'Donna', 'Shafi', 'Barbara', 'Sally', 'Xiaoyuan', 'Anita',
          'Mary Coombs', 'Ellen', 'Jeri', 'Lucy', 'Audrey', 'Maria', 'Melanie', 'Joanna', 'Megan', 'Sarah', 'Kesha']


@get('/supygirls/project')
@view("supygirls")
def project():
    modl, namel = "_spy", "__author__.py"
    try:
        code_file = DS.get_file_contents(modl, '', namel)
        code = "{" + dcd(str.encode(code_file.content)).decode("utf-8")[1:-2]+"}"
        print('/supygirls/project ', code)
        code = json.loads(code)
        cenas = [(girl, code[girl.lower()]['author_nick'] if girl.lower() in code else 'livre') for girl in CGIRLS]
    except Exception as err:
        cenas = [(girl, 'livre') for girl in CGIRLS]
        print('/supygirls/project ', err)
    return dict(pagetitle="SuPyGirls", action="/supygirls/moduler/", claim="",
                title="SUPYGIRLS", image="miro.jpg", cenas=cenas)


@get('/supygirls/moduler/<name>')
@view("supygirls")
def modulerr(name):
    modl, namel = name, "__author__.py"
    try:
        code_file = DS.get_file_contents(modl, '', namel)
        code = "{" + dcd(str.encode(code_file.content)).decode("utf-8")[1:-2]+"}"
        print('/supygirls/moduler ', name, code)
        code = json.loads(code)
        cenas = [(girl, code[girl.lower()]['author_nick'] if girl.lower() in code else 'livre') for girl in GIRLS]
    except Exception as err:
        cenas = [(girl, 'livre') for girl in GIRLS]
        print('/supygirls/moduler ', err)
    return dict(
        pagetitle="SuPyGirls - {}".format(name), title=name, action="/supygirls/gamer/{}/".format(name),
        claim="{}/".format(name), image="garden.jpg", cenas=cenas)


@get('/supygirls/gamer/<mod>/<name>')
@view("gamer")
def gamer(mod, name):
    modl, namel = mod.lower(), name.lower()
    try:
        code_file = DS.get_file_contents(modl, namel)
        code = code_file.content
        # code = dcd(str.encode(code_file.content)).decode("utf-8")
    except Exception:
        code = "# " + ".".join([modl, namel, "main.py"])
        code = ecd(bytearray(code.encode("UTF8"))).decode("utf-8")

    return dict(
        pagetitle='SuPyGirls - {} - {}'.format(mod.capitalize(), name.capitalize()), title=name,
        modText=mod.capitalize(),
        nameText=name.capitalize(),
        image="supygirls_logo.png", mod=mod.replace(',', '_').lower(), code=code,
        brython_css=CSS, brython_js=JS,
        menu=[m.split(",") for m in MENU.split(":")])


def _gamer_claim(projecter, moduler=""):
    modl, namel = projecter if moduler else '_spy', "__author__.py"
    form_values = "author_nick author_name author_email author_org author_site author_public".split()
    code = {key: request.params[key] for key in form_values}
    key = moduler if moduler else projecter
    spy = str({key: code}).replace("'", '"')[1:-1] + ",\n"
    # coded = str(code).replace("'", '"')
    author_index = projecter if moduler else '_spy'
    action = "/supygirls/gamer/{}/".format(projecter)
    claim = "{}/".format(projecter) if moduler else ""
    filename = '__author__.py'
    try:
        print(author_index, projecter, filename, spy)
        code_status = DS.append_file(author_index, filename, spy)
        filename = '{}/__author__.py'.format(moduler) if moduler else '__author__.py'
        code_status += DS.create_file(projecter, filename, "{\n"+spy)
        print(code, filename)
        code_file = DS.get_file_contents(modl, '', namel)
        code = "{" + dcd(str.encode(code_file.content)).decode("utf-8")[1:-2]+"}"
        code = json.loads(code)
        cenas = [(girl, code[girl.lower()]['author_nick'] if girl.lower() in code else 'livre') for girl in GIRLS]
    except Exception as err:
        code_status = "Fail creating {}: {}".format(filename, err)
        cenas = [(girl, 'livre') for girl in GIRLS]
    return dict(
        pagetitle="SuPyGirls - {}".format(projecter), title=projecter, action=action, claim=claim,
        image="garden.jpg", cenas=cenas, status=code_status)


@post('/supygirls/__claim/<projecter>/')
@view("supygirls")
def gamer_claim(projecter):
    return _gamer_claim(projecter)


@post('/supygirls/__claim/<projecter>/<moduler>/')
@view("supygirls")
def gamer_moduler_claim(projecter, moduler):
    return _gamer_claim(projecter, moduler)


appbottle = default_app()
_ = appbottle

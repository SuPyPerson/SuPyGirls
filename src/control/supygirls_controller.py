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
.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
"""
from bottle import Bottle, get, view, post, request, default_app
from model.datasource import DS
import json

__author__ = 'carlo'


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
        code_file = DS.get_file_contents(modl,'', namel)
        print('/supygirls/project ', code_file.content+"}")
        code = json.loads(code_file.content+"}")
        cenas = [(girl, code[girl]['author_nick'] if girl in code else 'livre') for girl in CGIRLS]
        # code = dcd(str.encode(code_file.content)).decode("utf-8")
    except Exception as err:
        cenas = [(girl, 'livre') for girl in CGIRLS]
        print('/supygirls/project ', err)
    return dict(pagetitle="SuPyGirls", action="/supygirls/module/", title="SUPYGIRLS", image="miro.jpg", cenas=cenas)


@get('/supygirls/module/<name>')
@view("supygirls")
def moduler(name):
    cenas = [(girl, 'livre') for girl in GIRLS]
    return dict(
        pagetitle="SuPyGirls - {}".format(name), title=name, action="game/{}/".format(name),
        image="garden.jpg", cenas=cenas)
    try:
        code_file = DS.get_file_contents(modl,'', namel)
        print('/supygirls/project ', code_file.content+"}")
        code = json.loads(code_file.content+"}")
        cenas = [(girl, code[girl]['author_nick'] if girl in code else 'livre') for girl in CGIRLS]
        # code = dcd(str.encode(code_file.content)).decode("utf-8")
    except Exception as err:
        cenas = [(girl, 'livre') for girl in CGIRLS]
        print('/supygirls/project ', err)
    return dict(pagetitle="SuPyGirls", action="/supygirls/module/", title="SUPYGIRLS", image="miro.jpg", cenas=cenas)



@get('/supygirls/module/game/<mod>/<name>')
@view("gamer")
def gamer(mod, name):
    modl, namel = mod.lower(), name.lower()
    try:
        code_file = DS.get_file_contents(modl, namel)
        code = code_file.content
        # code = dcd(str.encode(code_file.content)).decode("utf-8")
    except Exception as err:
        code = "# " + ".".join([modl, namel, "main.py"])
        code = ecd(bytearray(code.encode("UTF8"))).decode("utf-8")

    return dict(
        pagetitle='SuPyGirls - {} - {}'.format(mod.capitalize(), name.capitalize()), title=name,
        modText=mod.capitalize(),
        nameText=name.capitalize(),
        image="supygirls_logo.png", mod=mod.replace(',', '_').lower(), code=code,
        brython_css=CSS, brython_js=JS,
        menu=[m.split(",") for m in MENU.split(":")])

appbottle = default_app()
_ = appbottle



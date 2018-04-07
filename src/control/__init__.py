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


"""Main.py is the top level script.
Loads the Bottle framework and mounts controllers.  Also adds a custom error
handler.
"""
import os
# name and list your controllers here so their routes become accessible.
# Enable debugging, which gives us tracebacks
project_server = os.path.dirname(os.path.abspath(__file__))
js_dir = os.path.join(project_server, '../view/stlib')
css_dir = os.path.join(project_server, '../view/css')
img_dir = os.path.join(project_server, '../view/image')
py_dir = os.path.join(project_server, '../view')
print("js_dir = ", js_dir)

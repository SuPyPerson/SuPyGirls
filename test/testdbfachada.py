#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SuPyGirls
# Copyright 2013-2014 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# SuPyGirls é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser  útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
#  a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, escreva para a Fundação do Software
# Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
############################################################
SuPyGirls - Teste de Base de dados
############################################################

Verifica a funcionalidade do serviço de armazenamento.

"""
__author__ = 'carlo'
import unittest
import sys

import model.database as dbs
import model.datasource as dsrc

if sys.version_info[0] == 2:
    from mock import MagicMock
else:
    from unittest.mock import MagicMock


class SpyDBTest(unittest.TestCase):
    class WhiteBoxPyGithub:
        """
        Encapsulate assertions to calls in PyGithub API
        """
        def __init__(self):
            self.source = dsrc.DS = MagicMock(name="gitsrc")

        def assert_filexists(self, project, moduler):
            self.source.get_file_contents.return_value = "# uva main.py"
            self.source.get_file_contents.assert_called_once_with(project, moduler)

        def assert_file_updated(self, project, moduler, content="# updated uva main.py"):
            self.source.update_file.return_value = content
            self.source.update_file.assert_called_once_with(project, moduler, content)

        def assert_modules(self, project):
            self.source.get_branches.return_value = ["uva", "abacate"]
            self.source.get_branches.assert_called_once_with(project)

    def setUp(self):
        self.db = dbs.DB
        self.wb = SpyDBTest.WhiteBoxPyGithub()

    def test_default_page(self):
        """project and module must exist and module in session"""
        self.db.login("supyjogo", "uva")
        self.wb.assert_filexists("supyjogo", "uva")
        pass

    def test_load_module(self):
        """module content must be: # uva main.py"""
        self.db.load("supyjogo", "uva")
        self.wb.assert_filexists("supyjogo", "uva")
        pass

    def test_save_module(self):
        """module content must be: # updated uva main.py"""
        self.db.save(project="supyjogo", moduler="uva", content="# updated uva main.py")
        self.wb.assert_file_updated("supyjogo", "uva", "# updated uva main.py")
        pass

    def test_find_modules(self):
        """modules must be: ["uva", "abacate"]"""
        self.db.modules("supyjogo")
        self.wb.assert_modules("supyjogo")
        pass

    def test_ismember(self):
        """modules must be: ["uva", "abacate"]"""
        self.db.ismember("supyjogo", "uva")
        self.wb.assert_modules("supyjogo")
        pass


'''
    @classmethod
    def modules(cls, project):
        return Project.modules(project)

    @classmethod
    def ismember(cls, project, person):
        if not project:
            return Package.get(project, person)
        return Project.ismember(project, person)

    @classmethod
    def islogged(cls, project, person):
        project = Project.get(project)
        return project.islogged(person)

    @classmethod
    def logout(cls, project, person):
        project = Project.get(project)
        project.removesession(person)

    @classmethod
    def login(cls, project, person):
        return Project.ismember(project, person)

    @classmethod
    def init_db_(cls):

        if "AUTH_DOMAIN" not in os.environ.keys():
            return
'''

if __name__ == '__main__':
    unittest.main()

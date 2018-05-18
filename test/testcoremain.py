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
import sys, os
# os.path.dirname(os.path.abspath(__file__))
project_home = os.path.abspath(os.path.join(os.path.join(__file__, '../../'), 'src'))
print(project_home)
# add your project directory to the sys.path
# project_home = u'/home/supygirls/dev/SuPyGirls/src'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from view._core.main import Main

import model.datasource as dsrc
from unittest.mock import MagicMock, ANY


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

    class MockBrython:
        document = MagicMock(name="document")
        window = MagicMock(name="window")
        html = MagicMock(name="html")
        alert = MagicMock(name="alert")
        ajax = MagicMock(name="ajax")
        timer = MagicMock(name="timer")
        storage = MagicMock(name="storage")
        codename = "ada.ada"
        code = "aMOhIHVtYSBtYcOnw6MgcXVlIMOpIGFxdWUgdm9jw6ogdsOq"  # """ZGF0YSB0byBiZSBlbmNvZGVk"""
        ajaxer = ajax.ajax = MagicMock(name="ajax_ajax")
        rq = ajax.ajax.return_value = MagicMock(name="ajax_ajax_ret")
        opener = rq.open = MagicMock(name="ajax_ajax_open")
        sender = rq.send = MagicMock(name="ajax_ajax_send")


    def setUp(self):
        self.wb = SpyDBTest.WhiteBoxPyGithub()
        self.mb = SpyDBTest.MockBrython
        self.ds = Main._Main__save.display = MagicMock(name="display")
        self.mn = Main(SpyDBTest.MockBrython)

    def tearDown(self):
        self.mb.opener.reset_mock()
        self.mb.sender.reset_mock()

    def test_default_page(self):
        """project and module must exist and module in session"""
        assert self.mn
        pass

    def test_score(self):
        """should send score to github"""
        self.mn.scorer(dict(a=1, b=2))
        # self.ds.assert_any_call()
        self.mb.ajaxer.assert_any_call()
        self.mb.opener.assert_called_once_with('POST', '/game/__append_log', True)
        self.mb.sender.assert_any_call(ANY)
        send, _ = self.mb.sender.call_args_list[0]
        c1, c2 = "eydiJzogMiwgJ2EnOiAxfQ", "eydhJzogMSwgJ2InOiAyfQ"
        assert '"codename": "ada/__score__.py"' in send[0], "not in %s" % str(send[0])
        assert (c1 in send[0] or c2 in send[0]), "not in %s" % str(send[0])

    def test_save(self):
        """should send the dialog text value to github"""
        code = "aMOhIHVtYSBtYcOnw6MgcXVlIMOpIGFxdWUgdm9jw6ogdsOq"
        self.mn._save()
        self.mb.opener.assert_called_once_with('POST', '/game/__save', True)
        self.mb.sender.assert_any_call(ANY)
        send, _ = self.mb.sender.call_args_list[0]
        assert '"codename": "ada/main.py"' in send[0], "not in %s" % str(send[0])
        assert '"code": "{}'.format(code) in send[0], "not in %s" % str(send[0])


if __name__ == '__main__':
    unittest.main()

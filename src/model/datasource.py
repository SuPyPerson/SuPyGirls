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
SuPyGirls - Data Source
############################################################

Conecta com a fonte dos dados, neste caso a API do Github.

"""
import datetime
import os.path
import os as op
from github import Github
from base64 import decodebytes as dcd

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPackage/SuPyGirls.git"
USERNAME = "kwarwp"
PASSWORD = dcd(str.encode(op.environ["IKW"])).decode("utf-8")  # 'K004r00p## :=G1th00b'
# str(dcd(str.encode(op.environ["IKW"])))
# USERNAME = "carlotolla"
# PASSWORD = op.environ["ISME"]


def spike():

    g = Github(USERNAME, PASSWORD)
    u = g.get_user()
    r = None
    for repo in u.get_repos():
        if "SuPyGirls" in str(repo.name):
            r = repo
            break
        print(type(repo.name), repo.name)

    rp = u.get_repo("supyjogo")  # "activlets")

    print(r)
    [print(org) for org in rp.get_branches()]
    al = rp.get_branch("uva")
    cm = al.commit

    print(al.etag, al.commit.sha)
    print("cont", rp.get_file_contents("/uva/main.py", cm.sha).decoded_content)


class DataSource:
    def __init__(self):
        g = Github(USERNAME, PASSWORD)
        self.user = g.get_user()
        self.repo = None

    def get_file_branched(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        self.repo.get_branches()
        ref = self.repo.get_branch(packager).commit.sha
        return self.repo.get_file_contents("{}/{}".format(packager, moduler), ref)

    def get_file_contents(self, project, packager, moduler="main.py"):
        self.repo = self.user.get_repo(project)
        return self.repo.get_file_contents("{}/{}".format(packager, moduler))

    def update_file(self, project, packager, decoded_content, moduler="main.py", comment=None):
        timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        comment = comment if comment else "Automatic save at {}".format(timestamp)
        file = self.get_file_contents(project, packager)
        self.repo.update_file("{}/{}".format(packager, moduler), comment, decoded_content, file.sha)
        return comment

    def get_branches(self, project):
        self.repo = self.user.get_repo(project)
        return self.repo.get_branches()


DS = DataSource()

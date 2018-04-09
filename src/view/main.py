#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Kwarwp
# Copyright 2010-2018 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# Kwarwp é um software livre; você pode redistribuí-lo e/ou
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

"""Brython front end client.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
import json
from base64 import encodebytes as ecd

from view.kwarwp.supygirls_factory import GUI

CENAS = ["{}".format(chr(a)) for a in range(ord('a'), ord('z') + 1) if chr(a) not in 'aeiouy']
RMENU = "Edit,_edit:Open,_open"
MENU = [m.split(",") for m in RMENU.split(":")]
EMENU = [["Run", "_run"], ["Save", "_save"]]


class Main:
    def __init__(self, br):
        self.doc, self.ht, self.alert, self.storage = br.document, br.html, br.alert, br.storage
        self.ajax = br.ajax
        self.codename = codename = '{}.main.py'.format(br.codename)

        self.gui = GUI(code=br.code, codename=codename, br=br)
        self.dialog = None
        self.menu = dict(_edit=lambda *_: self._edit(),
                         _save=lambda *_: self._save(),
                         _open=lambda *_: self._open(),
                         _run=lambda *_: self._run(),
                         )

    def _edit(self):
        self.start(EMENU)
        self.dialog = self.gui.edit()

    def __save(self):
        def on_complete(request):
            if request.status == 200 or request.status == 0:
                self.doc["nav_saver"].html = request.text
            else:
                self.doc["nav_saver"].html = "error " + request.text
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        self.doc["nav_saver"].html = "Saving.. "+codename
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        # send a POST request to the url
        req.open('POST', "/game/save", True)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        code = ecd(bytearray(self.gui.code.encode("UTF8"))).decode("utf-8")
        req.send({'codename': codename, 'code': code})

    def _save(self):
        def display(msg):
            # self.doc["nav_saver"].style.transition = "opacity 4s"
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = msg
            # self.doc["nav_saver"].style.opacity = 0

        def on_complete(request):
            if request.status == 200 or request.status == 0:
                display(request.text)
            else:
                display("error " + request.text)
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        display("Saving.. "+codename)
        """
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        # send a POST request to the url
        req.open('POST', "/game/save", True)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        req.send({'codename': codename, 'code': self.gui.code})
        """
        # from html import unescape
        # from html.parser import HTMLParser

        code = ecd(bytearray(self.gui.code.encode("UTF8"))).decode("utf-8")
        # code = ecd(bytearray(HTMLParser().unescape(self.gui.code).encode("UTF8"))).decode("utf-8")
        jsrc = json.dumps({'codename': codename, 'code': code})
        # print(SAVE, jsrc)
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout('20000', lambda *_: display("NOT SAVED: TIMEOUT"))
        req.open('POST', "/game/__save", True)
        req.set_header('content-type', 'application/json')  # x-www-form-urlencoded')
        req.send(jsrc)

    def _open(self):
        ...

    def _run(self):
        dialog = self.gui.dialoger if self.gui.dialoger else self.dialog
        dialog.action(lambda *_: self.start())
        # self.gui.executa_acao(self.dialog, lambda *_: self.start())

    def start(self, navigate=MENU):
        ht = self.ht

        def do_menu(menu):
            menu.html = ""
            menus = [(ht.A(name, Class="nav-item is-tab"), ev) for name, ev in navigate]
            [menu <= item for item, ev in menus]
            [item.bind("click", self.menu[ev]) for item, ev in menus]
            menu <= ht.A('Home', Class="nav-item is-tab", href='/')

        do_menu(self.doc['right_menu'])
        do_menu(self.doc['burg_menu'])


def main(**kwargs):
    Main(**kwargs)


if __name__ == '__main__':
    main(**{})

PZ = ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua', 'argentina', 'armenia', 'australia',
      'austria', 'azerbaijan', 'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin',
      'bhutan', 'bolivia', 'bosnia', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina', 'burundi', 'cabo_verde',
      'cambodia', 'cameroon', 'canada', 'african_rep', 'chad', 'chile', 'china', 'colombia', 'comoros', 'dr_congo',
      'r_congo', 'costa_rica', 'ivoire', 'croatia', 'cuba', 'cyprus', 'czech_rep', 'denmark', 'djibouti', 'dominica',
      'dominican_rep', 'ecuador', 'egypt', 'el_salvador', 'eq_guinea', 'eritrea', 'estonia', 'ethiopia', 'fiji',
      'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea',
      'guinea-bissau', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq',
      'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait',
      'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania',
      'luxembourg', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall',
      'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco',
      'mozambique', 'myanmar', 'namibia', 'nauru', 'nepal', 'netherlands', 'new_zealand', 'nicaragua', 'niger',
      'nigeria', 'north_korea', 'norway', 'oman', 'pakistan', 'palau', 'palestine', 'panama', 'papua',
      'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda',
      'st_kitts', 'saint_lucia', 'st_vincent', 'samoa', 'san_marino', 'sao_tome', 'saudi_arabia',
      'senegal', 'serbia', 'seychelles', 'sierra_leone', 'singapore', 'slovakia', 'slovenia', 'solomon',
      'somalia', 'south_africa', 'south_korea', 'south_sudan', 'spain', 'sri_lanka', 'sudan', 'suriname', 'swaziland',
      'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga',
      'trinidad', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'emirates', 'united_kingdom',
      'america', 'uruguay', 'uzbekistan', 'vanuatu', 'vatican', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']

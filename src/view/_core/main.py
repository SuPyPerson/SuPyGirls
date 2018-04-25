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

from .supygirls_factory import GUI

CENAS = ["{}".format(chr(a)) for a in range(ord('a'), ord('z') + 1) if chr(a) not in 'aeiouy']
RMENU = "Edit,_edit"
# RMENU = "Edit,_edit:Open,_open"
MENU = [m.split(",") for m in RMENU.split(":")]
EMENU = [["Run", "_run"], ["Save", "_save"]]


class Main:
    def __init__(self, br):
        self.doc, self.ht, self.alert, self.storage = br.document, br.html, br.alert, br.storage
        self.ajax, self.timer = br.ajax, br.timer
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

    def _create(self):
        def change_color():
            self.doc["nav_saver"].style.transition = "opacity 0s"
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = ""

        def display(msg):
            self.timer.set_timeout(change_color, 15000)
            self.doc["nav_saver"].style.transition = "opacity 15s"
            # self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = msg
            self.doc["nav_saver"].style.opacity = 0

        def on_complete(request):
            if request.status == 200 or request.status == 0:
                display(request.text)
            else:
                display("error " + request.text)
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        display("Creating.. "+codename)
        code = ecd(bytearray(self.gui.code.encode("UTF8"))).decode("utf-8")
        # code = ecd(bytearray(HTMLParser().unescape(self.gui.code).encode("UTF8"))).decode("utf-8")
        jsrc = json.dumps({'codename': codename, 'code': code})
        # print(SAVE, jsrc)
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout('20000', lambda *_: display("NOT SAVED: TIMEOUT"))
        req.open('POST', "/game/__create", True)
        req.set_header('content-type', 'application/json')  # x-www-form-urlencoded')
        req.send(jsrc)

    def _create_log(self, error, log ="__log__.py"):
        def change_color():
            self.doc["nav_saver"].style.transition = "opacity 0s"
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = ""

        def display(msg):
            self.timer.set_timeout(change_color, 15000)
            self.doc["nav_saver"].style.transition = "opacity 15s"
            # self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = msg
            self.doc["nav_saver"].style.opacity = 0

        def on_complete(request):
            if request.status == 200 or request.status == 0:
                display(request.text)
            else:
                display("error " + request.text)
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-2] + [log])
        code = ecd(bytearray(error.encode("UTF8"))).decode("utf-8")
        # code = ecd(bytearray(HTMLParser().unescape(self.gui.code).encode("UTF8"))).decode("utf-8")
        jsrc = json.dumps({'codename': codename, 'code': code})
        # print(SAVE, jsrc)
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout('20000', lambda *_: display("NOT SAVED: TIMEOUT"))
        req.open('POST', "/game/__create", True)
        req.set_header('content-type', 'application/json')  # x-www-form-urlencoded')
        req.send(jsrc)

    def __append_log(self, error, log ="__log__.py"):
        def on_complete(request):
            if request.status == 200 or request.status == 0:
                self.doc["nav_saver"].html = request.text
            else:
                self.doc["nav_saver"].html = "error " + request.text

        codename = self.codename.split(".")
        codename = "/".join(codename[1:-2]+[log])
        code = ecd(bytearray(error.encode("UTF8"))).decode("utf-8")
        # code = ecd(bytearray(HTMLParser().unescape(self.gui.code).encode("UTF8"))).decode("utf-8")
        jsrc = json.dumps({'codename': codename, 'code': code})
        # print(SAVE, jsrc)
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        req.open('POST', "/game/__append_log", True)
        req.set_header('content-type', 'application/json')  # x-www-form-urlencoded')
        req.send(jsrc)


        """
        self.doc["nav_saver"].html = "Saving.. "+codename
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        # send a POST request to the url
        req.open('POST', "/game/__append", True)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        code = ecd(bytearray(error.encode("UTF8"))).decode("utf-8")
        req.send({'codename': codename, 'code': code})
        """

    def __save(self):
        def on_complete(request):
            if request.status == 200 or request.status == 0:
                self.doc["nav_saver"].html = request.text
            else:
                self.doc["nav_saver"].html = "error " + request.text

        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1]) + ".{}".format(codename[-1])
        self.doc["nav_saver"].html = "Saving.. "+codename
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        # send a POST request to the url
        req.open('POST', "/game/__save", True)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        # send data as a dictionary
        code = ecd(bytearray(self.gui.code.encode("UTF8"))).decode("utf-8")
        req.send({'codename': codename, 'code': code})

    def _save(self):
        def change_color():
            self.doc["nav_saver"].style.transition = "opacity 0s"
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = ""

        def display(msg):
            self.timer.set_timeout(change_color, 15000)
            self.doc["nav_saver"].style.transition = "opacity 15s"
            # self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = msg
            self.doc["nav_saver"].style.opacity = 0

        def on_complete(request, slf=self):
            if request.status == 200 or request.status == 0:
                if "404" in request.text:
                    self.timer.set_timeout(slf._create, 1000)
                    display("Attempting to create..")
                else:
                    display(request.text)
            else:
                display("error " + request.text)

        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        display("Saving.. "+codename)
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
        self.gui.error = self.error
        dialog.action(lambda *_: self.start()
                      )
        # self.gui.executa_acao(self.dialog, lambda *_: self.start())

    def error(self, error):
        self.__append_log(error)

    def start(self, navigate=MENU):
        ht = self.ht

        def do_ddmenu():
            ddmenu = ht.DIV(Class="navbar-item has-dropdown is-hoverable")
            ddmenu_ancora = ht.A("Open", Class="navbar-link")
            ddmenu <= ddmenu_ancora
            ddmenu_box = ht.DIV(Class="navbar-dropdown is-boxed")
            ddmenu <= ddmenu_box
            dmenus = [(ht.A(name, Class="navbar-item is-tab"), ev) for name, ev in [("main-0", " main_0")]]
            [ddmenu_box <= item for item, ev in dmenus]
            return ddmenu

        def do_menu(menu):
            menu.html = ""
            menus = [(ht.A(name, Class="navbar-item is-tab"), ev) for name, ev in navigate]
            [menu <= item for item, ev in menus]
            [item.bind("click", self.menu[ev]) for item, ev in menus]
            menu <= ht.A('Help', Class="navbar-item is-tab", href='/site/help.html')
            menu <= ht.A('About', Class="navbar-item is-tab", href='/site/about.html')
            menu <= ht.A('Home', Class="navbar-item is-tab", href='/')
            # menu <= do_ddmenu()

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

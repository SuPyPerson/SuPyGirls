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
import json, os
from base64 import encodebytes as ecd

from .supygirls_factory import GUI
from base64 import decodebytes as dcd

CENAS = ["{}".format(chr(a)) for a in range(ord('a'), ord('z') + 1) if chr(a) not in 'aeiouy']
RMENU = "Edit,_edit"
# RMENU = "Edit,_edit:Open,_open"
MENU = [m.split(",") for m in RMENU.split(":")]
EMENU = [["Run", "_run"], ["Save", "_save"]]


class Main:
    def __init__(self, br):
        self.doc, self.ht, self.alert, self.storage = br.document, br.html, br.alert, br.storage
        self.ajax, self.timer, self.window = br.ajax, br.timer, br.window
        self.codename = '{}.main.py'.format(br.codename)
        self.code, self.br = br.code, br
        # self.menu = dict(_edit=lambda *_: self._edit(),
        #                  _save=lambda *_: self._save(),
        #                  _open=lambda *_: self._open(),
        #                  _run=lambda *_: self._run(),
        #                  )
        self.menu = dict(_edit=self._edit,
                         _save=self._save,
                         _open=self._open,
                         _run=self._run,
                         )
        self.window.__SUPERPYTHON__ = self
        self.dialog = self.gui = None
        if "nav_saver" in self.doc:
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].style.margin = "15px"
            self.doc["nav_saver"].style.transition = "opacity 55s"

    def _edit(self, *_):
        self.doc['nav_waiter'].style.visibility = "visible"
        self.dialog = self.gui.edit()
        self.dialog.del_err()
        self.dialog.show()
        self.start(EMENU)

    def _create(self, content='', *_):
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        self.__save(codename, content, request_path='__create', action_name='Creating')

    def _create_log(self, error='', log="__log__.py", action_name='Creating Log'):
        codename = self.codename.split(".")
        # print("_create_log", codename, "/".join(codename[1:-2]+[log]))
        codename = "/".join(codename[1:-2] + [log])
        self.__save(codename, error, request_path='__create', action_name=action_name)

    def __append_log(self, error, log="__log__.py"):
        codename = self.codename.split(".")
        # print("__append_log", codename, "/".join(codename[1:-2]+[log]))
        codename = "/".join(codename[1:-2]+[log])
        self.__save(codename, error, lambda *_: self._create_log(error),
                    request_path="__append_log", action_name="Logging")

    def scorer(self, score, log="__score__.py"):
        codename = self.codename.split(".")
        codename = "/".join(codename[-4:-2]+[log])
        tabs = "  " * score.setdefault("_level", 0)
        # print("scorer", codename, "{}{},\n".format(tabs, score))
        self.__save(codename, "{}{},\n".format(tabs, score),
                    lambda *_: self._create_log(log="__score__.py", action_name=''),
                    request_path="__append_log", action_name="")

    def __save(self, codename, contents, creator=lambda *_: None, request_path="__save",
               action_name="Saving", address=None):
        def change_color():
            self.doc['nav_waiter'].style.visibility = "hidden"
            self.doc["nav_saver"].style.transition = "opacity 45s"
            self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].html = ""

        def display(msg, waiter="visible"):
            self.doc['nav_waiter'].style.visibility = waiter
            # self.doc["nav_saver"].style.opacity = 1
            self.doc["nav_saver"].style.transition = "opacity 45s"
            self.doc["nav_saver"].style.opacity = 0
            self.doc["nav_saver"].html = msg
            self.timer.set_timeout(change_color, 25000)

        def on_complete(request):
            if request.status == 200 or request.status == 0:
                if "404" in request.text:
                    self.timer.set_timeout(lambda *_: creator(contents), 1000)
                    display("Attempting to create..") if action_name else None
                else:
                    display(request.text,  waiter="hidden") if action_name else None
            else:
                display("error " + request.text)

        display("{}.. {}".format(action_name, codename)) if action_name else None
        code = ecd(bytearray(contents.encode("UTF8"))).decode("utf-8")
        # code = ecd(bytearray(HTMLParser().unescape(self.gui.code).encode("UTF8"))).decode("utf-8")
        jsrc = json.dumps({'codename': codename, 'code': code})
        # print(SAVE, jsrc)
        req = self.ajax.ajax()
        req.bind('complete', on_complete)
        req.set_timeout('20000', lambda *_: display("NOT SAVED: TIMEOUT"))
        address = address if address else "/game/{}".format(request_path)
        req.open('POST', address, True)
        req.set_header('content-type', 'application/json')  # x-www-form-urlencoded')
        req.send(jsrc)

    def _save(self, *_):
        codename = self.codename.split(".")
        codename = "/".join(codename[1:-1])+".{}".format(codename[-1])
        # print(" self.gui.dialogue:", codename, self.gui.get_code())
        self.__save(codename, self.gui.get_code(), self._create)

    def post_id(self, ev, form_id="ident-form", address='_claim/', *_):
        ev.preventDefault()
        self.doc["ident-modal"].className = "modal"
        contents = {el.name: el.value for el in self.doc[form_id].elements if "author" in el.name}
        # contents = str({el.name: el.value for el in self.doc[form_id].elements if "author" in name}).replace("'", '"')
        codename = self.codename.split(".")
        address = "/play/{}/{}/__claim/".format(codename[-4], codename[-3]) #, address)
        req = self.ajax.ajax()
        # print("post_id address", address, contents, codename)
        req.open('POST', address, True)
        req.bind('complete', lambda *_: None)
        req.set_header('content-type', 'application/x-www-form-urlencoded')  # x-www-form-urlencoded')
        req.send(contents)

    def _open(self, *_):
        ...

    def _run(self, *_):
        dialog = self.gui.dialogue if self.gui.dialogue else self.dialog
        self.gui.error = self.error
        dialog.action(lambda *_: self.start()
                      )
        # self.gui.executa_acao(self.dialog, lambda *_: self.start())

    def play(self):
        self.doc["ident-form"].bind('submit', self.post_id)
        # print("play codename:", self.codename)
        self.codename = ".".join(self.codename.split(".")[-4:])
        self.__play() if "_TEST_" in os.environ else self.timer.set_timeout(self.__play, 45000)

    def __play(self, *_):
        glob = dict(globals())
        glob.update(__name__="__main__")
        code = dcd(str.encode(self.code))
        # -XXX-  gambiarra para corrigir o brython
        codelist = list(code)
        codeclean = bytes(
            c for b, c, d in zip(codelist+[0, 0], [0]+codelist+[0], [0, 0]+codelist)
            if (c, d) != (194, 131) != (b, c))
        code = codeclean[1:-1].decode('utf-8')
        # -XXX- fim da gambiarra
        exec(code, glob)

    def error(self, error):
        date = self.window.Date().replace(
            ' GMT', '.{} GMt'.format(self.window.Date.new().getMilliseconds()))
        self.__append_log(
            "\n{{'date': '{} -X- SuPyGirls -X-',\n'error': '''{}'''}},".format(
                date, error))
        return error

    def start(self, navigate=MENU):
        ht = self.ht
        self.gui = self.gui if self.gui else GUI(code=self.code, codename=self.codename, br=self.br)
        self.dialog = self.gui.dialogue

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
        self.doc['nav_waiter'].style.visibility = "hidden"
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

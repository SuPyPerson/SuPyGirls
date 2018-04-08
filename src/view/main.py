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
from view.kwarwp.supygirls_factory import GUI
CENAS = ["{}".format(chr(a)) for a in range(ord('a'), ord('z') + 1) if chr(a) not in 'aeiouy']
RMENU = "Edit,_edit:Save,_save:Open,_open"
MENU = [m.split(",") for m in RMENU.split(":")]
EMENU = [["Run", "_run"]]


class Main:
    def __init__(self, br):
        self.doc, self.ht, self.alert, self.storage = br.document, br.html, br.alert, br.storage
        codename = '{}.main.py'.format(br.codename)
        self.gui = GUI(code='#{}'.format(codename), codename=codename, br=br)
        self.dialog = None
        self.menu = dict(_edit=lambda *_: self._edit(),
                         _save=lambda *_: self._save(),
                         _open=lambda *_: self._open(),
                         _run=lambda *_: self._run(),
                         )

    def _edit(self):
        self.start(EMENU)
        self.dialog = self.gui.edit()

    def _save(self):
        ...

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

    def _paint_scenes(self):
        """

        :return: 
        """
        ht = self.ht
        pyd = self.doc["pydiv"]
        pyd.html = ''
        sky = ht.DIV(style={'position': 'absolute', 'top': 0, 'left': 0})
        sky <= ht.IMG(src="image/sky.gif")
        sun = ht.DIV(
            id='the_sun', style={'position': 'absolute', 'top': 0, 'left': 0,
                                 'animation-name': 'daylight', 'animation-duration': '300s'})
        sun <= ht.IMG(src="image/sun.gif")
        pyd <= sky
        svg = ht.SVG(id="svgdiv", width="800", height="66")
        svg.setAttribute('height', "66")
        pyd <= svg
        pyd <= ht.DIV(id='selector', style={
            'position': 'relative', 'margin-top': '4px', 'display': 'flex',
            'max-width': '800px', 'flex-wrap': 'wrap', 'padding': '10px'})
        pyd <= sun

    def select_scene(self, scene):
        self.alert('foi' + scene)

    def paint_scenes(self):
        ht = self.ht
        self._paint_scenes()
        for count, scene in enumerate(CENAS):
            icon = ht.DIV(onclick=lambda *_: self.select_scene(scene))
            icon.setAttribute("style", 'flex:1;min-width: 160px; flex-wrap: wrap; margin: 10px;' +
                              'background-color: navajowhite; border-radius: 60px; padding:4px;')
            img = ht.IMG(src="image/garden.gif", width=60, title=scene,
                         style=dict(display='block', margin="0 auto"))
            style = {'width': '60px', 'height': '60px', 'padding': '20px', 'overflow': 'hidden',
                     'background': 'url(image/garden.jpg) no-repeat 0 0',
                     'background-position-x': '{}px'.format(-100 * (count % 5)),
                     'background-position-y': '{}px'.format(-100 * (count // 5))}

            # icon.onclick = lambda ev: self.select_scene(scene)
            img.onclick = lambda ev: self.select_scene(ev.target.title)
            div, span, legend = ht.DIV(style=style), ht.H6(scene, style={'text-align': 'center'}), ht.LEGEND(scene)
            # div <= img
            icon <= span
            icon <= div
            self.doc['selector'] <= icon


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

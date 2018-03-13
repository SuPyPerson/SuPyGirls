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

from random import choice, seed
from .kuarup import Kuarup

# seed()
IMAGEREPO = 'server_root/image/'
CANVASW, CANVASH = 800, 600
NODICT = {}
EDIT = "{}/{}".format(IMAGEREPO, "sun.gif")


#############################################################################

"""
page up 	33
page down 	34
end 	35
home 	36
left arrow 	37
up arrow 	38
right arrow 	39
down arrow 	40
insert 	45

"""


class Queue:
    def __init__(self):
        self.queue = []
        self.resolved = self.val = lambda *_: None

    def pop(self):
        if self.queue:
            yield self.queue.pop(0)
        else:
            yield lambda *_: None

    def push(self, item):
        self.queue.append(item)

    def run(self):
        while self.pop():
            pass


class TECLA:
    ACIMA = 38
    ABAIXO = 40
    DIREITA = 39
    ESQUERDA = 37

    BRANCO = 32
    ENTER = 13
    SOBE = 33
    DESCE = 34
    EMPURRA = 35
    PUXA = 36


class Dialog:
    def __init__(self, gui, text='xxxx', act=lambda x: None):
        self.text = text
        self._rect = gui.back(0, 66, 800, 540, 'black', '0.85')
        self._area = gui.textarea(text, 20, 80, 760, 500)
        self.edit = gui.edit
        gui.continua, self.continua = lambda *_: None, gui.continua
        self.gui = gui
        gui.edit = self.action
        self.act = act

    def remove(self):
        self._rect.remove()
        self._area.remove()

    def hide(self):
        self.remove()
        # self._rect.style.visibility = 'hidden'
        # self._area.style.visibility = 'hidden'

    def show(self):
        self._rect.style.visibility = 'visible'
        self._area.style.visibility = 'visible'

    def get_text(self):
        return self.text

    def set_text(self, text):
        self._area.value = text

    def action(self, event=None):
        self.text = self._area.value
        self.hide()
        self.act(self)
        self.gui.edit = self.edit
        self.gui.continua = self.continua


class EmpacotadorDeImagem:
    def __init__(self, canvas, glyph, x, y, dx, dy):
        self.canvas = canvas.svg  # .canvas
        self.render = canvas
        self.img = self.canvas.image(
            href=IMAGEREPO+glyph, x=x, y=y,
            height="{}px".format(dy), width="{}px".format(dx))
        self.x, self.y = x, y

    def __le__(self, other):
        other <= self.img

    def do_remove(self):
        self.img.remove()

    def remove(self):
        self.render.renderer(self.img, render=lambda: self.do_remove())

    def do_translate(self, x, y):
        self.x, self.y = self.x + x, self.y + y
        self.img.x, self.img.y = self.x, self.y

    def translate(self, x, y):
        self.render.renderer(self.img, render=lambda: self.do_translate(x, y))


class _GUI:
    def __init__(self, width, height, svg=None, document=None, html=None, cena=None, **kw):
        self.wsize = dict(width=width, height=height)
        self.queue = Queue()
        self.mundo_Kuarup = self.evs = None
        self.svg, self.html, self.cena = svg, html, cena
        self.evs = [getattr(TECLA, at) for at in dir(TECLA) if at.isupper()]
        document["svgdiv"].remove()
        self.svgpanel = svg.svg(id="svgdiv", width=width, height=height)
        document["pydiv"] <= self.svgpanel
        self.panel = document["svgdiv"]
        self.dom = document["pydiv"]
        self.document = document
        self.events = {}
        self.edit = self._edit
        self.dialogue = None

    def keyCode(self, ev):
        if ev.keyCode in self.evs:
            self.mundo_Kuarup.quandoApertaUmaTecla(ev.keyCode)
            ev.stopPropagation()

    def inicia(self, mundo, dx=0):
        self.wsize.update(width=dx) if dx else None
        self.panel.remove()
        # self.svgpanel = self.svg.svg(id="svgdiv", **self.wsize)
        self.dom <= self.svgpanel
        self.panel = self.document["svgdiv"]
        self.mundo_Kuarup = mundo
        self.document.bind("keypress", lambda ev: self.keyCode(ev))
        print("def inicia(self, mundo):", self.evs, mundo)

    def text(self, x, y, texto, color='navajowhite'):
        img = self.svg.text(
            texto, x=x, y=y,
            font_size=22, text_anchor="middle",
            style={"stroke": color, "fill": color})
        self.renderer(img)

    def renderer(self, img, render=None):
        if False:
            self.panel <= img

    def __render(self, img):
        def do_render(img):
            self.panel <= img
        self.queue.push(lambda: do_render(img))

    def back(self, x, y, dx, dy, color, opacity="1.0"):
        rec = self.svg.rect(x=x, y=y, width=dx, height=dy, stroke=color, fill=color,
                            style=dict(fillOpacity=opacity, visibility="visible"))
        self.panel <= rec
        return rec

    def rect(self, x, y, dx, dy, color, opacity="1.0"):
        img = self.svg.rect(x=x, y=y, width=dx, height=dy, stroke=color, fill=color,
                            style=dict(fillOpacity=opacity))
        self.renderer(img)
        return img

    def executa_acao(self, dialog):
        pass

    def _edit(self, *_):
        self.dialog("ola", act=self.executa_acao)

    def editor(self, glyph):
        glyph.bind('click', lambda *_: self._edit)

    def image(self, glyph, x, y, dx, dy):
        img = EmpacotadorDeImagem(self, glyph, x, y, dx, dy)
        if "sun.gif" in glyph:
            img.img.bind('click', lambda *_: self.edit())
            self.editor(img.img)
        self.renderer(img.img)
        return img

    def escolha(self, lista):
        return choice(lista)

    def textarea(self, text, x, y, w, h, style=NODICT):

        def dpx(d):
            return '%spx' % d

        attrs = {'position': 'absolute', 'top': dpx(y), 'left': dpx(x),
                 'width': dpx(w), 'height': dpx(h), 'resize': 'none', 'borderColor': 'darkslategrey',
                 'color': 'navajowhite', 'border': 1, 'background': 'transparent'}
        t = self.html.TEXTAREA(text, style=attrs)
        self.dom <= t
        return t

    def dialog(self, text, img=EDIT, act=lambda x: None):
        text = self.cena
        if self.dialogue:
            self.dialogue.remove()
        self.dialogue = Dialog(self, text=text, act=act)
        self.dialogue.set_text(text)
        self.dialogue.show()
        return self.dialogue


class GUI(_GUI):
    """ O terreno onde o Festival Kuarup é apresentado
    """

    def __init__(self, width=CANVASW, height=CANVASH, svg=None, document=None, html=None, cena=None):
        _GUI.__init__(self, width=width, height=height, svg=svg, document=document, html=html, cena=cena)
        self.executante = None
        self.queue = Queue()
        self.renderer = self.do_render

    def run(self):
        self.executante()

    def do_render(self, img, render=None):
        render() if render else self.panel <= img

    def _renderer(self, render=None):
        self.queue.push(lambda: render())

    def _render(self, img, render=None):
        self.queue.push(lambda: render() if render else self.do_render(img))

    def executa_acao(self, dialog):
        self.cena = dialog.get_text()
        self.renderer = self._render
        self.renderer = self.do_render
        exec(self.cena, globals())
        o_indio = Tchuk(Kuarup.CORREDOR_ROCHOSO, indio=Tchuk, gui=self)
        o_indio.inicia()

    def registra_executante(self, executante):
        self.renderer = self._render
        self.executante = executante
        executante()

    def espera(self):
        pass

    def continua(self):
        print("def continua(self):", len(self.queue.queue))
        self.queue.pop().__next__()()

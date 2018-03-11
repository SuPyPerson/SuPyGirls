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

# seed()
IMAGEREPO = 'server_root/image/'
CANVASW, CANVASH = 800, 600


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


class EmpacotadorDeImagem:
    def __init__(self, canvas, glyph, x, y, dx, dy):
        self.canvas = canvas  # .canvas
        self.img = self.canvas.image(
            href=IMAGEREPO+glyph, x=x, y=y,
            height="{}px".format(dy), width="{}px".format(dx))
        self.x, self.y = x, y

    def __le__(self, other):
        other <= self.img

    def remove(self):
        self.img.remove()

    def translate(self, x, y):
        self.x, self.y = self.x + x, self.y + y
        self.img.x, self.img.y = self.x, self.y


class _GUI:
    def __init__(self, width, height, svg, document):
        self.mundo_Kuarup = self.evs = None
        self.svg = svg
        self.evs = [getattr(TECLA, at) for at in dir(TECLA) if at.isupper()]
        self.panel = document["svgdiv"]

        # document["keyCodeKeydown"].bind("keydown", self.keyCode)
        document.bind("keypress", self.keyCode)
        # document["keyCodeKeyup"].bind("keyup", self.keyCode)
        self.events = {}

    def keyCode(self, ev):
        if ev.keyCode in self.evs:
            self.mundo_Kuarup.quandoApertaUmaTecla(ev.keyCode)
            ev.stopPropagation()

    def inicia(self, mundo):
        self.mundo_Kuarup = mundo
        print("def inicia(self, mundo):", self.evs)
        # mundo.inicia()

    def Return(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.ENTER)

    def space(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.BRANCO)

    def Right(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.DIREITA)

    def Left(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.ESQUERDA)

    def Up(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.ACIMA)

    def Down(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.ABAIXO)

    def Next(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.DESCE)

    def Prior(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.SOBE)

    def Home(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.EMPURRA)

    def End(self, ev): self.mundo_Kuarup.quandoApertaUmaTecla(TECLA.PUXA)

    def text(self, x, y, texto, color='navajowhite'):
        img = self.svg.text(
            texto, x=x, y=y,
            font_size=22, text_anchor="middle",
            style={"stroke": color, "fill": color})
        self.panel <= img

    def rect(self, x, y, dx, dy, color):
        img = self.svg.rect(x=x, y=y, width=dx, height=dy, stroke=color, fill=color)
        self.panel <= img

    def image(self, glyph, x, y, dx, dy):
        img = EmpacotadorDeImagem(self.svg, glyph, x, y, dx, dy)
        self.panel <= img.img
        return img

    def escolha(self, lista):
        return choice(lista)


class GUI(_GUI):
    """ O terreno onde o Festival Kuarup é apresentado
    """

    def __init__(self, width=CANVASW, height=CANVASH, svg=None, document=None):
        _GUI.__init__(self, width=width, height=height, svg=svg, document=document)
        self.executante = None

    def run(self):
        self.executante()

    def registra_executante(self, executante):
        self.executante = executante

    def espera(self):
        pass

    def continua(self):
        pass

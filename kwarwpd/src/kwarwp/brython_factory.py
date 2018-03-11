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
from threading import Event, Thread

from . import svgcanvas as gi
from .svgcanvas import *

seed()
IMAGEREPO = '/image/'


#############################################################################

class TECLA:
    ACIMA = 111
    ABAIXO = 116
    DIREITA = 114
    ESQUERDA = 113

    BRANCO = 65
    ENTER = 36
    SOBE = 112
    DESCE = 117
    EMPURRA = 97
    PUXA = 103


class _GUI(gi.GUI):
    def inicia(self, mundo):
        self.mundo_Kuarup = mundo

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

    def rect(self, x, y, w, h, **kwargs):
        gi.GUI.rect(self, x, y, w - x, h - y, **kwargs)

    def image(self, href, x, y, w, h, **kwargs):
        """ Returns an Image
        x,y - position; w,h - size
        """
        parent = kwargs.pop(PARENT, self)
        return Image(IMAGEREPO + href, x=x, y=y, width=w, height=h,
                     parent=parent, **kwargs)

    def escolha(self, lista):
        return choice(lista)


class GUI(_GUI):
    """ O terreno onde o Festival Kuarup é apresentado
    """

    def __init__(self, width=CANVASW, height=CANVASH):
        _GUI.__init__(self, width=width, height=height)
        self.executante = None
        self.evento = Event()

    def run(self):
        self.executante()

    def registra_executante(self, executante):
        self.executante = executante
        self.evento = Event()
        Thread.__init__(self)
        self.start()

    def espera(self):
        self.evento.wait()
        self.evento.clear()

    def continua(self):
        self.evento.set()

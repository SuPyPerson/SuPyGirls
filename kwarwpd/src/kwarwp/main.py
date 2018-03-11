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
from .kuarup import Kuarup
from .brython_factory import GUI


class Queue:
    def __init__(self):
        self.queue = []

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


class Main:

    def __init__(self, params):
        self.queue = Queue()
        self.count = 0
        self.doc, self.svg, self.ww = params
        self.panel = self.doc["svgdiv"]
        self.title = None
        self.settings()
        self.mundo = Kuarup(gui=GUI(svg=self.svg, document=self.doc))
        self.mundo.inicia()

    def settings(self):
        print("def main(doc, svg)")
        self.title = self.svg.text(
            'LOADING..', x=200, y=30,
            font_size=22, text_anchor="middle",
            style={"stroke": "yellow", "fill": "yellow"})
        self.panel <= self.title
        self.doc["svg_circle"].bind('click', self.mouseclick)
        self.fill()

    def fill(self, *_):
        for it in range(0, 10):
            self.queue.push(self.paint)

    def paint(self, *_):
        self.count += 1
        self.title.textContent = "Contagem {}".format(self.count)

    def mouseclick(self, *_):
        nexter = self.queue.pop().__next__()
        print("self.queue.pop().__next__()", nexter)
        nexter()


def main(doc, svg, ww):
    Main((doc, svg, ww))


if __name__ == '__main__':
    main([], "", None)

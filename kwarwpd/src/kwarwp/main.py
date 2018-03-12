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

function timeoutPromise (time) {
  return new Promise(function (resolve) {
    setTimeout(function () {
      resolve(Date.now());
    }, time)
  })
}

function doSomethingAsync () {
  return timeoutPromise(1000);
}

async function doAsync () {
  var start = Date.now(), time;
  console.log(0);
  time = await doSomethingAsync();
  console.log(time - start);
  time = await doSomethingAsync();
  console.log(time - start);
  time = await doSomethingAsync();
  console.log(time - start);
}

doAsync();
"""
from .kuarup import Kuarup
from .brython_factory import GUI


class Queue:
    def __init__(self, promise, timer):
        self.queue = []
        self.promise = promise.Promise
        self.async = promise.doAsync
        self.tout = timer.set_timeout
        self.resolved = self.val = lambda *_: None

    def timeoutPromise(self):
        def resolver(resolve, rej, sf=self):
            if sf.queue:
                item = sf.queue.pop(0)
                resolve(item)
                return item
            else:
                rej(lambda *_: None)
                return lambda *_: None
        return self.promise.new(lambda resolve, rej: self.tout(lambda: resolver(resolve, rej), 1000))

    def get(self):
        def promise():
            return self.timeoutPromise()

        def res(val):
            self.val = val
            print("def get(self):def res(val)", self.val)
            return val
        result = self.async(promise)  # .then(res)
        # print("def get(self):", result.then(res))
        result.then(res, res)  # lambda *_: None
        val, self.val = self.val, lambda *_: None
        return val  # lambda *_: None

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
        self.count = 0
        self.doc, self.svg, self.ww, self.tt = params
        self.Promise = self.ww.Promise
        self.queue = Queue(self.ww, self.tt)
        self.panel = self.doc["svgdiv"]
        self.title = None
        # asyncio.ensure_future(process_file())
        self.queue.push(self.paint)
        self.queue.push(self.paint)
        print("self.queue.pop().__next__()")
        self.settings()
        return
        self.mundo = Kuarup(Kuarup.CORREDOR_ROCHOSO, gui=GUI(svg=self.svg, document=self.doc))
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
        def value(res):
            pass
        for it in range(0, 10):
            res = self.queue.get()
            print("def value(res):", res)
            # res() if hasattr(res, '__call__') else None
            res()

    def paint(self, *_):
        self.count += 1
        self.title.textContent = "Contagem {}".format(self.count)

    def mouseclick(self, *_):
        self.queue.push(self.paint)
        print("self.queue.pop().__next__()")

    def _mouseclick(self, *_):
        nexter = self.queue.pop().__next__()
        print("self.queue.pop().__next__()", nexter)
        nexter()


def main(doc, svg, ww, tt):
    Main((doc, svg, ww, tt))


if __name__ == '__main__':
    main([], "", None)

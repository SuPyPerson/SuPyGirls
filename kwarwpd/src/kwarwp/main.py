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
import asyncio
import random
from asyncio import sleep, coroutine


q = asyncio.Queue(10)


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

        print("def main(doc, svg)")
        self.panel = self.doc["svgdiv"]
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


@asyncio.coroutine
def _produce():
    while True:
        yield from q.put(random.random())
        print("yield from q.put(random.random())")
        # yield from asyncio.sleep(0.5 + random.random())


@asyncio.coroutine
def _consume():
    while True:
        print("To be Consumed", q.qsize())
        value = yield from q.get()
        print("Consumed", value)


@asyncio.coroutine
def produce():
    while True:
        yield from asyncio.ensure_future(q.put(random.random()))
        print("yield from q.put(random.random())")
        # yield from asyncio.sleep(0.5 + random.random())


@asyncio.coroutine
def consume():
    while True:
        print("To be Consumed", q.qsize())
        value = yield from asyncio.ensure_future(q.get())
        print("Consumed", value)


def tallyman(w, ww):
    # w = ww.WorkerParent('kwarwp/worker.py', [1, 2, 3], {"test": "Ahoj"})
    m = ww.Message('ping', "ahoj")
    print("ww.Message('ping'", m)
    r = w.post_message(m, want_reply=True)
    print("w.post_message(m, want_reply=True)", r)
    w.post_message(ww.Message('quit', None))


@coroutine
def tally(w):
    # Wait for the worker to start
    yield w.wait_for_status(ww.S_RUNNING)

    print("w.wait_for_status(ww.S_RUNNING)", w)
    # Call the remote add method
    a = yield w.add(10, 20)
    assert a == 30

    # Call the remote log method
    yield w.log("Test output")

    # Destroy the worker
    w.terminate()


count = 0


def main(doc, svg, ww):
    Main((doc, svg, ww))


def _main(doc, svg, ww):
    print("def main(doc, svg)")
    panel = doc["svgdiv"]
    title = svg.text('LOADING..', x=200, y=30,
                     font_size=22, text_anchor="middle",
                     style={"stroke": "yellow", "fill": "yellow"})
    panel <= title

    def mouseclick(*_):
        global count
        count += 1
        title.textContent = "Contagem {}".format(count)
        produce()
    doc["svg_circle"].bind('click', mouseclick)

    print("ww.RPCWorkerParent")
    # w = ww.RPCWorkerParent('kwarwp/worker.py',[1,2,3],{"USER":"nobody"})

    # Run the main method
    # tally(w)
    # print("ensure_future(produce(0))", asyncio.ensure_future(produce()))
    # print("ensure_future(produce(1))", asyncio.ensure_future(produce()))
    # print("ensure_future(produce(2))", asyncio.ensure_future(produce()))
    loop = asyncio.get_event_loop()
    print("ensure_future(produce(0))", asyncio.ensure_future(produce()))
    print("ensure_future(produce(1))", asyncio.ensure_future(produce()))
    print("ensure_future(consume(0))", asyncio.ensure_future(consume()))
    print("ensure_future(consume(1))", asyncio.ensure_future(consume()))
    print("ensure_future(consume(2))", asyncio.ensure_future(consume()))
    print("ensure_future(consume(3))", asyncio.ensure_future(consume()))
    loop = asyncio.get_event_loop()


if __name__ == '__main__':
    main([], "", None)

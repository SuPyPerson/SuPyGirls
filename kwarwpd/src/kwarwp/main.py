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
from .kuarupfest import Mapas
CENAS = [
    'INICIO', 'ROCHAS', 'CORREDOR', 'CORREDOR_ROCHOSO', 'ZIGZAG', 'CARACOL',
    'BETUMES', 'BETUMES_ROCHAS', 'POR_ONDE', 'RECORDAR_E_VIVER', 'PISA_NA_FULO',
    'MIRAFLOR',
    ]


class Cenas:
    CORREDOR_ROCHOSO = '''class Tchuk(Kuarup):
    """ O personagem controlado pelo jogador conectado
    """

    def define_comportamento(self):
        self.fala('olá a todos')
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.direita()
        self.direita()
        self.anda()
    
    '''

    def __init__(self):
        pass


class Tchuk(Kuarup):
    """ O personagem controlado pelo jogador conectado
    """

    def define_comportamento(self):
        self.fala('olá a todos')
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.direita()
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.direita()
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.direita()
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.esquerda()
        self.larga()
        self.direita()
        self.direita()
        self.anda()
        self.pega()
        self.anda()
        self.anda()
        self.direita()
        self.anda()


class Main:

    def __init__(self, **kwargs):
        self.count, self.kwargs = 0, kwargs
        self.doc, self.svg, self.cena, self.ht = [kwargs[key] for key in 'doc svg cena html'.split()]
        code = getattr(Cenas, self.cena, Cenas.CORREDOR_ROCHOSO)
        cena = getattr(Kuarup, self.cena, Kuarup.CORREDOR_ROCHOSO)
        self.scene = kwargs['cena'] = cena
        kwargs['code'] = code
        # kwargs = dict(svg=self.svg, document=self.doc, html=self.ht, win=wd, cena=cena)
        # self.panel = self.doc["svgdiv"]
        self.title = self.mundo = None
        # self.settings()

    def start(self, scene):
        cena = getattr(Kuarup, scene, Kuarup.CORREDOR_ROCHOSO)
        self.kwargs.update(cena=cena)
        gui = GUI(self.paint_scenes, **self.kwargs)
        self.doc["pydiv"].html = ""
        self.mundo = Kuarup(cena, indio=Tchuk, gui=gui)
        self.mundo.inicia()

    def settings(self):
        # asyncio.ensure_future(process_file())
        print("self.queue.pop().__next__()")
        print("def main(doc, svg)")
        self.title = self.svg.text(
            'LOADING..', x=200, y=30,
            font_size=22, text_anchor="middle",
            style={"stroke": "yellow", "fill": "yellow"})
        self.panel <= self.title
        self.doc["svg_circle"].bind('click', self.mouseclick)
        # self.fill()

    def _fill(self, *_):
        def value(res):
            pass
        for it in range(0, 10):
            res = self.queue.get()
            print("def value(res):", res)
            # res() if hasattr(res, '__call__') else None
            res()

    # def fill(self, *_):
    #     for it in range(0, 10):
    #         self.queue.push(self.paint)

    def paint(self, *_):
        self.count += 1
        self.title.textContent = "Contagem {}".format(self.count)

    def _mouseclick(self, *_):
        print("self.queue.pop().__next__()")

    def mouseclick(self, *_):
        # nexter = self.queue.pop().__next__()
        print("self.queue.pop().__next__()", nexter)
        # nexter()

    def select_scene(self, scene):
        self.start(scene)

    def _paint_scenes(self):
        """
                    <div style="position: absolute; top=0; left=0;">
                <img src="server_root/image/sky.gif"/>
            </div>
            <div id='the_sun' style="position: absolute; top=0; left=0;
             animation-name: daylight; animation-duration: 300s">
                <img src="server_root/image/sun.gif"/>
            </div>
            <svg id="svgdiv" width="800" height="66"></svg>
            <div id="selector" style="position: relative; margin-top: 4px;
            display:flex; max-width: 800px; flex-wrap: wrap; padding:10px;"></div>

        :return: 
        """
        ht = self.ht
        pyd = self.doc["pydiv"]
        pyd.html = ''
        sky = ht.DIV(style={'position': 'absolute', 'top': 0, 'left': 0})
        sky <= ht.IMG(src="server_root/image/sky.gif")
        sun = ht.DIV(
            id='the_sun', style={'position': 'absolute', 'top': 0, 'left': 0,
                                 'animation-name': 'daylight', 'animation-duration': '300s'})
        sun <= ht.IMG(src="server_root/image/sun.gif")
        pyd <= sky
        svg = ht.SVG(id="svgdiv", width="800", height="66")
        svg.setAttribute('height', "66")
        pyd <= svg
        pyd <= ht.DIV(id='selector', style={
            'position': 'relative', 'margin-top': '4px', 'display': 'flex',
            'max-width': '800px', 'flex-wrap': 'wrap', 'padding': '10px'})
        pyd <= sun

    def paint_scenes(self):
        ht = self.ht
        self._paint_scenes()
        for scene in CENAS:
            the_scene = scene
            icon = ht.DIV(onclick=lambda *_: self.select_scene(scene))
            icon.setAttribute("style", 'flex:1;min-width: 160px; flex-wrap: wrap; margin: 10px;' +
                              'background-color: navajowhite; border-radius: 60px; padding:4px;')
            img = ht.IMG(src="server_root/image/saida.gif", width=60, title=scene,
                         style=dict(display='block',  margin="0 auto"))
            # icon.onclick = lambda ev: self.select_scene(scene)
            img.onclick = lambda ev: self.select_scene(ev.target.title)
            div, span, legend = ht.DIV(), ht.H6(scene, style={'text-align': 'center'}), ht.LEGEND(scene)
            div <= img
            icon <= span
            icon <= div
            self.doc['selector'] <= icon


def main(**kwargs):
    Main(**kwargs)


if __name__ == '__main__':
    main(**{})

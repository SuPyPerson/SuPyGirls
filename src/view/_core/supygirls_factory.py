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
import sys
import traceback
from random import random
from base64 import decodebytes as dcd

random()
IMAGEREPO = 'server_root/image/'
CANVASW, CANVASH = 800, 600
NODICT = {}
EDIT = "{}/{}".format(IMAGEREPO, "sun.gif")
EDTST = {'position': 'relative', 'padding': 10, 'margin': '0', 'flex': '3 1 auto',
         'width': '99%', 'resize': 'none', 'borderColor': 'darkslategrey',
         'color': 'navajowhite', 'border': 1, 'background': 'rgba(10, 10, 10, 0.5)'}
ERRST = {'position': 'relative', 'padding': 10, 'margin': '0', 'visibility': 'visible', 'flex': '1',
         'width': '99%', 'min-height': '30%', 'resize': 'none', 'borderColor': 'darkslategrey',
         'color': 'navajowhite', 'border': 1, 'background': 'rgba(200, 54, 54, 0.5)'}
CSLST = {'position': 'relative', 'padding': 10, 'margin': '0', 'visibility': 'visible', 'flex': '1',
         'width': '99%', 'min-height': '30%', 'resize': 'none', 'borderColor': 'darkslategrey',
         'color': 'navajowhite', 'border': 1, 'background': 'rgba(74, 200, 74, 0.5)'}


#############################################################################


class Dialog:
    def __init__(self, gui, text='xxxx', act=lambda *_: False):

        divat = {'position': 'absolute', 'top': 0, 'left': 0, 'display': 'flex', 'padding': '7px',
                 'flex-direction': 'column', 'align-items': 'stretch',
                 'width': '100%', 'height': '100%', 'background': 'rgba(10, 10, 10, 0.85)'}
        self.text = text
        self.gui = gui
        self.html, self.dom = gui.html, gui.dom
        self._div = self._err = self._area = None
        self._div = self._div if self._div else self.html.DIV(style=divat)
        self.dom <= self._div
        text = text if text else self.text
        self._area = self.textarea(text, style=EDTST)
        self._set_code(text)
        self.act = act

    def _set_code(self, *_):
        def set_hint(cm):
            self.gui.window.CodeMirror.simpleHint(cm, self.gui.window.CodeMirror.pythonHint)
        self._div <= self._area
        self.__area = self.gui.window.CodeMirror.fromTextArea(
            self._area, dict(
                mode="python", theme="solarized", lineNumbers=True, indentUnit=4,
                tabSize=4, smartIndent=False))
        self.gui.window.CodeMirror.commands.autocomplete = set_hint
        self._doc = self.__area.getDoc()

    def textarea(self, text, style=EDTST):
        t = self.html.TEXTAREA(text, style=style)
        return t

    def remove(self):
        self._div.remove()

    def hide(self):
        self.remove()

    def show(self):
        self._div.style.visibility = 'visible'

    def _update_text(self):
        # self.text = self._area.val()
        self.text = self._doc.getValue()  # self._area.value
        return self.text

    def get_text(self):
        self.__area.save()
        self.text = ''
        # return self._doc.getValue()  # self.text if self.text else self._update_text()
        return self._update_text()

    def set_csl(self, text):
        self._err.remove() if self._err else None
        self._err = self.textarea(text, style=CSLST)
        self._div <= self._err
        self.text = ''

    def set_err(self, text):
        self._err.remove() if self._err else None
        self._err = self.textarea(text, style=ERRST)
        self._div <= self._err
        self.text = ''
        error = text
        lines = error.split(' line ')
        if len(lines) > 1:
            try:
                line = int(lines[-1].split("\n")[0])
                _ = error.split("\n")[-2]
                _ = self._doc.setSelection(dict(line=line - 1, ch=0), dict(line=line - 1, ch=60))
            except Exception as x:
                print("Exception", x)

    def del_err(self):
        self._err.remove() if self._err else None
        self._err = None

    def set_text(self, text):
        self._area.value = text

    def action(self, extra):
        self.text = self._area.value
        # self.hide()
        self.act(self, lambda *_: self.hide() or extra()) if self.act else None


class EmpacotadorDeImagem:
    def __init__(self, canvas, glyph, x, y, dx, dy):
        self.canvas = canvas  # .canvas
        self.render = canvas
        self.img = self.canvas.image(
            href=IMAGEREPO + glyph, x=x, y=y,
            height="{}px".format(dy), width="{}px".format(dx))
        self.x, self.y = x, y

    def __le__(self, other):
        other <= self.img

    def do_remove(self):
        self.img.remove()

    def remove(self):
        pass
        self.render.renderer(self.img, render=lambda: self.do_remove())

    def do_move(self, x, y, image=None):
        self.img.x, self.img.y = x, y
        if image:
            self.img.href.baseVal = IMAGEREPO + image

    def mover(self, x, y, image=None, *_, **__):
        self.x, self.y = x, y
        self.render.renderer(self.img, render=lambda: self.do_move(x, y, image))

    def do_translate(self, x, y):
        self.x, self.y = self.x + x, self.y + y
        self.img.x, self.img.y = self.x, self.y

    def translate(self, x, y):
        self.render.renderer(self.img, render=lambda: self.do_translate(x, y))


class _GUI:
    def __init__(self, br, **kw):
        self.doc, self.html, self.alert, self.storage = br.document, br.html, br.alert, br.storage
        self.window = br.window
        self.dom = self.doc["pydiv"]
        self.document = self.doc
        self.events = {}
        self.edit = self._edit
        self.dialogue = self.code = None

    def executa_acao(self, dialog):
        return False

    def _edit(self, *_):
        return self.dialog("", act=self.executa_acao)

    def image(self, glyph, x, y, dx, dy):
        img = EmpacotadorDeImagem(self, glyph, x, y, dx, dy)
        return img

    def textarea(self, text, style=EDTST):
        divat = {'position': 'absolute', 'top': 64, 'left': 0,
                 'width': '800px', 'height': '536px', 'background': 'rgba(10, 10, 10, 0.85)'}
        # divat = {'position': 'absolute', 'top': dpx(y), 'left': dpx(x),
        #          'width': dpx(w), 'height': dpx(h), 'background': 'rgba(10, 10, 10, 0.85)'}
        d = self.html.DIV(style=divat)
        t = self.html.TEXTAREA(text, style=style)
        d <= t
        self.dom <= d
        return t

    def dialog(self, text=None, act=lambda *_: False):
        text = text if text else self.code
        if self.dialogue:
            self.dialogue.remove()
        self.dialogue = Dialog(self, text=text, act=act)
        self.dialogue.set_text(text)
        self.dialogue.show()
        return self.dialogue

    def continua(self):
        pass


class GUI(_GUI):
    """ O terreno onde o Festival Kuarup é apresentado
    """

    def __init__(self, width=CANVASW, height=CANVASH, code="", codename="", **kwargs):
        _GUI.__init__(self, width=width, height=height, **kwargs)
        self.code, self.codename = dcd(str.encode(code)).decode("utf-8"), codename
        self.error = self.extra = self.dialoger = None

    def _first_response(self, dialog, action, extra, error):
        class ConsoleOutput:

            def __init__(self):
                self.value = ''

            def write(self, data):
                self.value += str(data)

            def flush(self):
                self.value = ''
                pass

        value = self.value = ConsoleOutput()
        sys_out, sys.stdout = sys.stdout, value
        sys_err, sys.stderr = sys.stderr, value
        # logger('first response %s %s %s' % (dialog, sys.stdout, sys.stderr))
        # TODO action += self.challenge[1]
        # logger('first response code %s' % action)
        try:
            dialog = self.dialoger if self.dialoger else dialog
            self.code = dialog.get_text()
            # self.dialoger = None
            action()
            '''
            extra()
            self.dialoger = None
            '''
            console = str(self.value.value)
            if console:
                self.dialoger = self.dialog(self.code, act=self.executa_acao)
                self.dialoger.set_csl(console)
            else:
                self.dialoger = None
                extra()
        except Exception as err:
            # except Exception as err:
            traceback.print_exc(file=sys.stderr)
            sys.stdout = sys_out
            sys.stderr = sys_err
            err_trace = self.value.value
            annotated_error = error(str(err_trace))
            self.dialoger = self.dialog(self.code, act=self.executa_acao)  # +str(self.value.value))
            self.dialoger.set_err(annotated_error)
            # print(self.code)
            # self.dialoger = None
            return False
        sys.stdout = sys_out
        sys.stderr = sys_err
        return True

    def _executa_acao(self):
        glob = dict(globals())
        glob.update(__name__="__main__")
        exec(self.code, glob)  # dict(__name__="__main__"))

    def executa_acao(self, dialog, action=None):
        self.extra = action if action else lambda *_: None
        self.error = self.error if self.error else lambda *_: print("NO NO", self.error)
        self.code = dialog.get_text()
        self.storage[self.codename] = self.code
        return self._first_response(dialog, lambda: self._executa_acao(), self.extra, self.error)

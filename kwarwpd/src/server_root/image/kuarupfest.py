#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Kuarup - Festival de jogos na aprendizagem de Python
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2011/02/19  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2010, `GPL <http://is.gd/3Udt>__. 
"""
__author__  = "Carlo E. T. Oliveira (cetoli@yahoo.com.br) $Author: cetoli $"
__version__ = "1.0 $Revision$"[10:-1]
__date__    = "2011/02/19 $Date$"


import Tkinter
from threading import Event, Thread
from kuarup import MundoKuarup, TECLA
from random import choice, seed
seed()
IMAGEREPO = 'image/'

    
#############################################################################
MAPA = [
    ("^","ar","sky.gif",(10,4)),
    ("*","fixo","cercado.gif"),
    ("+","grande","pedra.gif"),
    ("@","variante","piche.gif"),# "voce ficou grudado"),
    ("O","pesado","tronco.gif"),
    ("&","fragil","flor.gif"),
    ("%","varigrande","onca.gif"),
    ("x","saida","saida.gif"),
    ("=","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",".**********.*@+O&&%%@*.*@a==*=@=x.**********")]
MAPA = [
    ("^","ar","sky.gif",(10,4)),
    ("=","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",".a=")]
class Mapas:
    INICIO = [
    ("^","ar","sky.gif",(10,4)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("w","grudante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",''',oooooo,ow...x,o....o,o....o,o.a.ro,oooooo''')
        
    ]
    ROCHAS = [
    ("^","ar","sky.gif",(10,4)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("w","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
ooooooo
o..o..x
o..r..o
oa.o..o
ooooooo''')
    ]
    CORREDOR = [
    ("^","ar","sky.gif",(10,4)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("w","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
oooooooooooooo
oa...........x
oooooooooooooo''')
    ]
    CORREDOR_ROCHOSO = [
    ("^","ar","sky.gif",(10,4)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("w","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
oooooooooooooo
oa.rrrrrrrrr.x
oooooooooooooo''')
    ]
    ZIGZAG = [
    ("^","ar","sky.gif",(15,10)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("w","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
oooooooooooooo
o............x
o.oooooooooooo
o.o...........
o.oooooooooooo
o............o
oooooooooooo.o
...........o.o
oooooooooooo.o
oa...........o
oooooooooooooo''')
    ]
    BETUMES = [
    ("^","ar","sky.gif",(15,10)),
    ("o","fixo","cercado.gif"),
    ("r","grande","pedra.gif"),
    ("W","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
ooxoo
o...o
oWoWo
o.a.o
ooooo''')
    ]
    BETUMES_ROCHAS = [
    ("^","ar","sky.gif",(15,10)),
    ("o","fixo","cercado.gif"),
    ("R","varigrande","pedra.gif"),
    ("W","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
ooxoo
o...o
oRoRo
o.o.o
o.o.o
oWoWo
o.a.o
ooooo''')
    ]
    CARACOL = [
    ("^","ar","sky.gif",(15,13)),
    ("o","fixo","cercado.gif"),
    ("R","varigrande","pedra.gif"),
    ("W","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
oooooooooooooo
o............o
o.oooooooooo.o
o.o........o.o
o.o.oooooo.o.o
o.o.o....o.o.o
o.o.o.oo.o.o.o
o.o.o.xo.o.o.o
o.o.oooo.o.o.o
o.o......o.o.o
o.oooooooo.o.o
o..........o.o
oooooooooooo.o
oa...........o
oooooooooooooo''')
    ]
    POR_ONDE = [
    ("^","ar","sky.gif",(15,13)),
    ("o","fixo","cercado.gif"),
    ("R","varigrande","pedra.gif"),
    ("W","variante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
.oooooooooooo
.o.......o..x
.o.o.o.o.o.oo
.o.o.o.o.o.o.
.oWoWoWoWoWo.
.o.o.o.o.o.o.
oo.o.o.o.o.o.
oa...oR..R.o.
oooooooooooo.''')
    ]
    PISA_NA_FULO = [
    ("^","ar","sky.gif",(15,13)),
    ("o","fixo","cercado.gif"),
    ("&","fragil","flor.gif"),
    ("r","grande","pedra.gif"),
    ("t","pesado","tronco.gif"),
    ("m","grudante","livre.gif"),
    ("w","grudante","piche.gif"),
    ("x","saida","saida.gif"),
    (".","caminho"),("a","ator","smkp-%s0%s.gif"),
    ("#","cenario","soil.gif",'''
.oooooooooooo
.om.om.o...mo
.om&&&&m.m.oo
.om&mm&m&&&o.
.om&&m&&&m&o.
.o.m&m.m.mto.
oo.m&mmmmmro.
oam.&&&&&awx.
oooooooooooo.''')
]

#############################################################################

class EmpacotadorDeImagem:
    def __init__(self, canvas, glyph, x, y, dx, dy):
        self.canvas = canvas
        self.pi = Tkinter.PhotoImage(file = IMAGEREPO + glyph)
        self.imageinstance = self.canvas.create_image(
            x,y, image = self.pi,anchor = Tkinter.NW)
        self.x,self.y = x, y
    def remove(self):
        self.canvas.delete(self.imageinstance)
    def translate(self,x,y):
        self.x,self.y= self.x +x , self.y+y
        self.canvas.coords(self.imageinstance,self.x,self.y)

class Kuarup(Thread):
    def __init__(self):
        self.top = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(
            self.top, bg="forest green", height=640, width=800)
        self.canvas.pack()
        EVENTOS = {"<Return>":self.Return,"<space>":self.space,
           "<Right>":self.Right,"<Left>":self.Left,
           "<Up>":self.Up,"<Down>":self.Down,
           "<Next>":self.Next,"<Prior>":self.Prior,
           "<Home>":self.Home,"<End>":self.End}

        for evento, lidador in EVENTOS.items():
            self.top.bind_all(evento,lidador)
        
    def text(self,x,y,texto,color='navajo white'):
        self.canvas.create_text(x,y,text=texto , fill=color,
                                font=("Helvectica", "16"))# width=0)
    def rect(self,x,y,dx,dy,color):
        self.canvas.create_rectangle(x,y,dx,dy, fill=color, width=0)
    def image(self,glyph,x,y,dx,dy):
        img = EmpacotadorDeImagem(self.canvas,glyph,x,y,dx,dy)
        return img
    def inicia(self):
        self.mundo_Kuarup = MundoKuarup(self,MAPA)
        self.top.mainloop()
    def run(self):
        self.executante()
    def registra_executante(self,executante):
        self.executante= executante
        self.evento = Event()
        Thread.__init__(self)
        self.start()
    def espera(self):
        self.evento.wait()
        self.evento.clear()
    def continua(self):
        self.evento.set()
        
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

    def escolha(self, lista):
        return choice(lista)
    
if __name__ == "__main__":
    mundo = Kuarup()
    mundo.inicia()



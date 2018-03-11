#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Kuarup - Festival de jogos na aprendizagem de Python
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2012/03/18  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2010, `GPL <http://is.gd/3Udt>__. 
"""
__author__ = "Carlo E. T. Oliveira (cetoli@yahoo.com.br) $Author: cetoli $"
__version__ = "1.0 $Revision$"[10:-1]
__date__ = "2011/02/13 $Date$"

from kwarwp.kuarup import Kuarup
from kwarwp.tkinter_factory import GUI


class Tchuk(Kuarup):
    """ O personagem controlado pelo jogador conectado 
    """

    def define_comportamento(self):
        self.fala('olá a todos')
        self.direita()
        self.anda()
        self.pega()
        self.esquerda()
        self.anda()
        self.larga()
        self.direita()
        self.anda()
        self.esquerda()
        self.anda()
        self.anda()
        self.direita()
        self.anda()


# INICIO, CORREDOR, ZIGZAG, CARACOL, CORREDOR_ROCHOSO
# BETUMES, ROCHAS, BETUMES_ROCHAS, POR_ONDE,PISA_NA_FULO
if __name__ == "__main__":
    mundo = Tchuk(Kuarup.CORREDOR_ROCHOSO, Tchuk, gui=GUI)
    # mundo = Tchuk(Kuarup.RECORDAR_E_VIVER,Tchuk)
    mundo.inicia()

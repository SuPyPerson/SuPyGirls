#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Kuarup - Festival de jogos na aprendizagem de Python
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2011/02/13  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2010, `GPL <http://is.gd/3Udt>__. 
"""
__author__  = "Carlo E. T. Oliveira (cetoli@yahoo.com.br) $Author: cetoli $"
__version__ = "1.1 $Revision$"[10:-1]
__date__    = "2011/02/19 $Date$"

import time

HS=48
HX, HY = 1,0
STEPX, STEPY = 32, 32
DX, DY = 0,0
GX, GY = 0,0
TEXTX, TEXTY = 400,96
CANVASW, CANVASH = 800,640
HDX, HDY = DX-8,DY-14
TWO1DR = range(-2,3)
TWO2DR = [(x,y) for x in TWO1DR for y in TWO1DR]
FABRICA,ARGUMENTOS = 0, 1
GLIFO,NOME,IMAGEM,GRADE = 0, 1, 2, 3

class TECLA: 
    ACIMA=111
    ABAIXO=116
    DIREITA=114
    ESQUERDA=113

    BRANCO=65
    ENTER=36
    SOBE=112
    DESCE=117
    EMPURRA=97
    PUXA=103

#def enum(*sequential, **named):
#    enums = dict(zip(sequential, range(len(sequential))), **named)
#    return type('Enum', (), enums)
#
#TECLA = enum(ACIMA=111,ABAIXO=116,DIREITA=114,ESQUERDA=113,
#             BRANCO=65,ENTER=36,SOBE=112,DESCE=117,EMPURRA=97,PUXA=103)
class Elemento:
    TEMPO = 0
    def __init__(self, x=0, y=0, imgxy= int(HS * 0.7), imagem = None):
        """ Um elemento básico do Jogo.
        """
        self.x, self.y = x, y
        self.imgxy = imgxy
        self.image = self
        if imagem: self.glifo_imagem = imagem
       
    def atravessa(self, movimento):
        movimento()

    def remove(self):
        pass
    
    def abandona(self, movimento, x=0, y=0):
        movimento()

    def empurrando(self, x, y, dx, dy, movement,canvas):
        pass
    
    def move(self, x, y, movimento, canvas):
        self.x, self.y = x, y
        self.pinta(canvas)
        movimento()
        
    def entra(self, cenario, x=0, y=0):
        self.cenario = cenario
        self.x, self.y = x, y
        return self
    def sai(self, movimento, x=0, y=0):
        pass
    def olha(self, x=0, y=0):
        return self.glifo_imagem.split('.')[0]
    def pega(self, movimento, x=0, y=0):
        pass
    def larga(self, movimento, x=0, y=0):
        pass
        
    def fabricar(self,construtor, *argumento):
        pass
    
    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '', imagem = '', *args):
        instancia = fabrica(x = x, y = y)
        if imagem:
            instancia.glifo_imagem = imagem
            instancia.pinta(canvas)
        return instancia
    
    def pinta(self, canvas):
        imgxy = self.imgxy
        self.image.remove()
        self.image = canvas.image(
            self.glifo_imagem, self.x*STEPX+DX, self.y*STEPY+DY, imgxy, imgxy)

class Ar(Elemento):
    def fabricar(self,construtor, *argumento):
        global DX,DY,HDX,HDY,GX,GY
        GX, GY = argumento[GRADE]
        GX, GY = GX * 16, GY * 16
        DX = CANVASW/2 - GX
        DY = CANVASH/2 - GY
        HDX, HDY = DX-8,DY-7
 
class Animado(Elemento):
    def entra(self, terreno, x, y):
        """ o personagem avança para um novo terreno"""
        self.terreno = self.implemento = terreno
        return Empty()
    def remove(self):
        """ método inócuo para usar o personagem como uma imagem nula"""
        pass
        
    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '', imagem = ''):
        self.canvas, self.image = canvas, self
        self.cria_vetor_de_imagens(imagem)
        self.x , self.y = self.vaiX, self.vaiY = x, y
        self.pinta(canvas, x, y)
        self.acoes = {TECLA.ABAIXO:self.somos_da_patria_amada,
                    TECLA.ACIMA:self.em_frente_marche,
                    TECLA.DIREITA:self.direita_volver,
                    TECLA.ESQUERDA:self.esquerda_volver,
                    TECLA.SOBE:self.apresentar_armas,
                    TECLA.DESCE:self.des_can_saar,
                    TECLA.ENTER:self.luzes_camera_acao,
                    TECLA.BRANCO:self.somos_da_patria_amada,
                    TECLA.EMPURRA:self.empurrar,
                    TECLA.PUXA:self.empurrar}
        return self
    
    def define_comportamento(self):
        pass

    def cria_vetor_de_imagens(self,imagem):
        self.cardinames = [c for c in 'nesw']
        cardinals=[(0,1),(1,0),(0,-1),(-1,0),]
        self.cardinals = dict(zip(self.cardinames,cardinals))
        self.heroImages = [imagem%(direction,"%d") for direction in self.cardinames]
        self.numHero = 3
        self.nextHead = 0
        self.curHero = 0

    def pinta(self, canvas, x=0, y=0, posicao_heroi=0):
        self.image.remove()
        self.curHero = posicao_heroi or self.curHero + 1
        self.curDirection = self.nextHead
        self.x,self.y = self.vaiX, self.vaiY
        self.curHero = self.curHero % self.numHero
        nx, ny = self.x * STEPX + HDX, self.y * STEPY + HDY
        himage = self.heroImages[self.curDirection]
        self.image = canvas.image(himage%self.curHero, nx, ny, HS, HS)
        
    def movimenta(self, direcao=None, x=10, y=10):
        """ Move um heroi
        """
        self.nextHead = direcao
        dx,dy = self.cardinals[self.cardinames[self.nextHead]]
        self.vaiX,self.vaiY = self.x+dx,self.y-dy
        self.terreno.move(
            self.vaiX,self.vaiY, self.vai_e_move, self.canvas)
        self.implemento.move(self.vaiX,self.vaiY, self.remove, self.canvas)
        
    def acao(self, evento):
        """ Age como um heroi
        """
        self.acoes[evento]()
        
    def em_frente_marche(self):
        self.terreno.avanca_tempo()
        self.terreno.abandona(
            lambda self=self, head=self.nextHead:self.movimenta(self.nextHead),
            self.x,self.y)
        
    def direita_volver(self):
        self.terreno.avanca_tempo()
        self.nextHead = abs((self.nextHead + 1) % 4)
        self.vaiX, self.vaiY = self.x, self.y
        self.pinta(self.canvas, posicao_heroi = 1)
    def esquerda_volver(self):
        self.terreno.avanca_tempo()
        self.nextHead = (self.nextHead - 1) % 4
        self.vaiX, self.vaiY = self.x, self.y
        self.pinta(self.canvas, posicao_heroi = 1)
    def aa_pon_tar(self):
        dx,dy = self.cardinals[self.cardinames[self.nextHead]]
        vaix, vaiy = self.vaiX, self.vaiY = self.x+dx,self.y-dy
        return self.terreno.olha(vaix, vaiy)
    def somos_da_patria_amada(self,texto=None):
        #self.r = self.canvas.rect(100,66,700,128,'forest green')
        if texto :
            self.canvas.text(TEXTX,TEXTY,texto)
        else:
            self.canvas.text(TEXTX,TEXTY,self.aa_pon_tar())
    def des_can_saar(self):
        self.terreno.avanca_tempo()
        dx,dy = self.cardinals[self.cardinames[self.nextHead]]
        vaix, vaiy = self.vaiX, self.vaiY = self.x+dx,self.y-dy
        self.implemento.empurrando(self.x, self.y, dx, dy, self.larga_o_implemento, self.canvas)
        #self.implemento.larga(self.larga_o_implemento,vaix, vaiy)
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        movement()
    def empurrar(self):
        self.terreno.avanca_tempo()
        dx,dy = self.cardinals[self.cardinames[self.nextHead]]
        self.vaiX, self.vaiY = self.x+dx,self.y-dy
        self.terreno.empurrando(self.vaiX, self.vaiY, dx, dy,
            self.em_frente_marche, self.canvas)
    def apresentar_armas(self):
        self.terreno.avanca_tempo()
        dx,dy = self.cardinals[self.cardinames[self.nextHead]]
        self.vaiX, self.vaiY = self.x+dx,self.y-dy
        self.terreno.pega(self.pega_o_implemento, self.vaiX, self.vaiY)
    def pega_o_implemento(self, implemento):
    		if self.implemento != self.terreno: return
        self.implemento = implemento
        self.implemento.move(self.x, self.y, self.remove, self.canvas)
    def larga_o_implemento(self):
        #self.implemento.move(
        #    self.vaiX, self.vaiY, self.remove, self.canvas)
        #self.terreno.adentra(self.implemento,self.vaiX,self.vaiY)
        self.implemento = self.terreno
    def inicia_comportamento(self):
        self.canvas.registra_executante(self.define_comportamento)
        self.inicia_comportamento= self.remove
    def luzes_camera_acao(self):
        self.inicia_comportamento()
        self.canvas.continua()
    def _avanca_tempo(self):
        self.canvas.espera()
    def executa_passo(self, comando, *arg):
        self._avanca_tempo()
        return comando(*arg)
       
    def vai_e_move(self):
        """ Move um heroi
        """
        self.pinta(self.canvas)

class Personagem(Animado):
    """ O personagem controlado pelo jogador conectado 
    """
    def olha(self):
        """ Olha o que vem por ai
        """
        return self.executa_passo(self.aa_pon_tar)
    def fala(self, *arg):
        """ Olha o que vem por ai
        """
        return self.executa_passo(self.somos_da_patria_amada, *arg)
    def anda(self):
        """ Move um heroi
        """
        return self.executa_passo(self.em_frente_marche)
    def direita(self):
        """ Move um heroi
        """
        return self.executa_passo(self.direita_volver)
    def pega(self):
        """ Pega (n)um objeto adiante
        """
        return self.executa_passo(self.apresentar_armas)
    def empurra(self):
        """ Empurra um objeto adiante
        """
        return self.executa_passo(self.empurrar)
    def larga(self):
        """ Larga (d)um objeto adiante
        """
        return self.executa_passo(self.des_can_saar)
    def esquerda(self):
        """ Move um heroi
        """
        return self.executa_passo(self.esquerda_volver)

class Fixo(Elemento):

    def atravessa(self,movement):
        pass

class Passante(Fixo):

    def atravessa(self,movement):
        movement()
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        movement()
    def pinta(self, canvas):
        pass
        
class Grudante(Fixo):

    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '',
              imagem = '', *args):
        instancia = fabrica(x = x, y = y)
        instancia.texto = args and args[0] or 'Você ficou grudado para sempre!'
        instancia.canvas = canvas
        if imagem:
            instancia.glifo_imagem = imagem
            instancia.pinta(canvas)
        return instancia
    def atravessa(self,movement):
        self.r = self.canvas.rect(100,66,700,128,'forest green')
        self.canvas.text(400,96,self.texto)
        movement()
    def abandona(self,movement,x=0,y=0):
        pass
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        movement()

class Saida(Fixo):

    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '',
              imagem = '', *args):
        instancia = fabrica(x = x, y = y)
        instancia.texto = args and args[0] or 'Você achou a saída!'
        instancia.canvas = canvas
        if imagem:
            instancia.glifo_imagem = imagem
            instancia.pinta(canvas)
        return instancia
    def atravessa(self,movement):
        self.r = self.canvas.rect(100,66,700,128,'forest green')
        self.canvas.text(400,96,'Você achou a saída!')

        movement()
    def abandona(self,movement,x=0,y=0):
        pass
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        movement()
        
class Variante(Grudante):
    VAZIO = None

    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '', imagem = '', *args):
        if Variante.VAZIO == None: Variante.VAZIO = canvas.escolha([True,False])
        if Variante.VAZIO:
            instancia = Empty()#Passante(x,y, int(HS*0.2), imagem = 'livre.png')
            Variante.VAZIO = False
        else:
            Variante.VAZIO = True
            instancia = fabrica(x = x, y = y)
            instancia.texto = args and args[0] or 'Você ficou grudado para sempre!'
            if imagem:
                instancia.glifo_imagem = imagem
                instancia.pinta(canvas)
        instancia.canvas = canvas
        return instancia

class Grande(Elemento):
        
    def atravessa(self,movement):
        pass
    def pega(self, movimento, x=0, y=0):
        self.cenario.sai(self,self.x,self.y)

        movimento(self)
    def larga(self, movimento, x=0, y=0):
        self.cenario.move(x,y, movimento)
    def sai(self,movimento, x, y):
        self.cenario.sai(self, x, y)
        self.x, self.y = x, y
        movimento(self)
    def move(self, x, y, movimento, canvas):
        self.cenario.move(
            x,y,lambda self=self:self.vai_e_move(x, y, movimento,canvas))
    def vai_e_move(self, x, y, movimento, canvas):
        self.x, self.y = x, y
        self.pinta(canvas)
        movimento() 
        
    def empurrando(self, x, y, dx, dy, movimento, canvas):
        nx, ny = self.x + dx, self.y -dy
        self.cenario.empurrando(nx, ny, dx, dy,
            lambda self=self, x = nx, y=ny, m = movimento, c= canvas
                :self.vai_e_empurra(x, y,m,c),
            canvas)
    def vai_e_empurra(self, nx, ny, movimento,  canvas):
        self.cenario.sai(self, self.x, self.y)
        self.cenario.adentra(self, nx, ny)
        self.x, self.y = nx, ny
        self.pinta(canvas)
        movimento() 

class Pesado(Grande):
    def pega(self, movimento, x=0, y=0):
        pass
    def larga(self, movimento, x=0, y=0):
        pass

class Fragil(Elemento):
    def pega(self, movimento, x=0, y=0):
        self.cenario.sai(self, self.x, self.y)
    def larga(self, movimento, x=0, y=0):
        self.cenario.sai(self, self.x, self.y)
    def atravessa(self, movimento):
        self.cenario.sai(self, self.x, self.y)
        movimento()
    def empurrando(self, x, y, dx, dy, movimento, canvas):
        self.cenario.sai(self, self.x, self.y)
        movimento()
     
        
class Varigrande(Grande):
    VAZIO = None

    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '', imagem = '', *args):
        if Varigrande.VAZIO == None: Varigrande.VAZIO = canvas.escolha([True,False])
        if Varigrande.VAZIO:
            instancia = Passante(x,y, int(HS*0.2), imagem = 'livre.png')
            Varigrande.VAZIO = False
        else:
            Varigrande.VAZIO = True
            instancia = fabrica(x = x, y = y)
            if imagem:
                instancia.glifo_imagem = imagem
                instancia.pinta(canvas)
        return instancia
    
class Cenario(Elemento):
        
    def fabricar(self,construtor, *argumento):
        self.instance = construtor.fabricar_instancia(DX,DY,'#')
        construtor.inventario['#'][FABRICA] = self
        cenario, separador = argumento[GRADE][1:], argumento[GRADE][0]
        self.grade = construtor.fabricar_grade(cenario.split(separador),self)
    
    def criar(self, canvas, fabrica, x, y, glifo= '' , nome = '', imagem = '', *args):
        instancia = fabrica(x = x, y = y)
        instancia.temporizados = []
        grade = args[0][1:].split(args[0][0])
        imgxy = int(HS*0.7)
        nx, ny = len(grade[0]), len(grade)
        instancia.ceu = canvas.image(
            'sky.gif', 0, 0, CANVASW, imgxy)
        c = 800
        x = c/2
        y=(x*x /c) /20
        instancia.sol = canvas.image(
            'sun.gif', 0, y-10, imgxy, imgxy)
        instancia.solpos = (-c/ 2, c /10 , c/2)
        if imagem:
            instancia.glifo_imagem = imagem
        canvas.rect(
            DX, DY, DX+nx*imgxy, DY+ny*imgxy,'navajo white')
        return instancia
    
    def registra_tempo(self, registrado):
        self.temporizados.append(registrado)
    def avanca_tempo(self):
        """ Move o astro no céu
        """
        x, y, c = self.instance.solpos
        nx, ny = x+2,  (x*x /c) /10.0 +40
        self.instance.solpos = nx, ny, c
        self.instance.sol.translate(nx-x,ny-y)
        Elemento.TEMPO +=1
        for elemento in self.instance.temporizados:
            elemento.avanca_tempo() 
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        self.grade[y][x].empurrando(x, y, dx, dy, movement, canvas)
    
    def move(self, x, y, movement,canvas=None):
        """ Move um heroi
        """
        self.grade[y][x].atravessa(movement)
        return
        if (x < 0) or (y < 0) : return
        try:
          self.grade[y][x].atravessa(movement)
        except: pass
        
    def abandona(self, movimento, x=0, y=0):
        self.grade[y][x].abandona(movimento)
    
    def adentra(self, implemento, x, y):
        """ Entra um implemento no cenário
        """
        self.grade[y][x].image.remove()
        self.grade[y][x]=implemento
        return
    def sai(self, implemento, x, y):
        """ Sai um implemento do cenário
        """
        implemento.image.remove()
        self.grade[y][x]=Empty()
        return
    def olha(self, x=0, y=0):
        """ Move um heroi
        """
        return self.grade[y][x].olha(x, y)
    def pega(self, acao, x, y,canvas=None):
        """ Move um heroi
        """
        self.grade[y][x].pega(acao,x, y)
        return
        #if (x < 0) or (y < 0) : return
        try:
          self.grade[y][x].sai(acao,x, y)
        except: pass   
    def pinta(self, canvas):
        pass

class Empty(Elemento):
        
    def empurrando(self, x, y, dx, dy, movement,canvas=None):
        """ Empurra um item
        """
        movement()
    def pinta(self, canvas):
        pass
    def olha(self, x=0, y=0):
        return 'livre'

INVENTARIO = {'ar':Ar,'cenario':Cenario,'caminho':Empty, 'variante':Variante,
             'fixo':Fixo, 'ator':Personagem,  'grande':Grande,'saida':Saida,
             'passante':Passante, 'varigrande':Varigrande, 'grudante':Grudante,
             'fragil':Fragil, 'pesado':Pesado}
        
class MundoKuarup:
    """ O terreno onde o Festival Kuarup é apresentado
    """

    @classmethod
    def get_canvas_size(self):
        """Possibilita o teste substituir o canvas por um arremedo"""
        return 1024,800
    def __init__(self,canvas, mapa_de_configuracao, canvas_x= 800, canvas_y = 640):
        """ Standard initialiser.
        """
        global CANVASW, CANVASH
        CANVASW, CANVASH = canvas_x, canvas_y
        self.canvas = canvas
        
        self.constroi_inventario_de_classes(mapa_de_configuracao)
        self.hero = self.inventario['a'][FABRICA]
        try:
            self.canvas.set_background_rect(DX,DY,GX,GY)
        except AttributeError:
            pass

    def constroi_inventario_de_classes(self, inventario):
        """ Cria a descrição das classes disponíveis no inventário
        """
        self.inventario = dict(
            [(item[GLIFO],[INVENTARIO[item[NOME]](),item])
                for item in inventario])
        fabrica = self.inventario['^']
        fabrica[FABRICA].fabricar(self, *fabrica[ARGUMENTOS])
        for fabrica in self.inventario.values():
            fabrica[FABRICA].fabricar(self, *fabrica[ARGUMENTOS])
        
    def fabricar_instancia(self,x,y,tipo_de_classe):
        classe_a_fabricar = self.inventario[tipo_de_classe]
        fabrica_criada = classe_a_fabricar[FABRICA]
        argumentos = classe_a_fabricar[ARGUMENTOS]
        classe_fabricante = INVENTARIO[argumentos[NOME]]
        instancia_fabricada = fabrica_criada.criar(
            self.canvas, classe_fabricante, x, y, *argumentos)
        return instancia_fabricada
    
    def fabricar_grade(self,cenario,terreno):
        return [[self.fabricar_instancia(x,y,row[x]).entra(terreno,x,y)
                 for x in range(len(row))]
            for y, row in enumerate(cenario)]
        
    def quandoDisparaTemporizador(self, timerID):
        """ Acontece toda vez que o temporizador dispara.
        """
        pass
    
    def quandoApertaUmaTecla(self,ev):
        self.hero.acao(ev)
        pass

    
#############################################################################
#MAPA = [("*","cerca","fence.gif"),("+","grande","stone.gif"),("=","caminho"),("a","ator","smkp-%s0%s.gif"),("#","cenario","soil.gif","**********.*++======*.*=a==*===*.**********")]
#MAPA = "00~*&cerca&fence.gif^=&caminho^a&ator&smkp-%s0%s.gif~**********.*a=======*.*========*.**********~00"
#############################################################################

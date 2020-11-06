.. _Tutorial_Vitollino:

**Tutorial Vitollino**
=======================
 
.. image:: _static/6_plataf_pacote.png

.. Warning:: 
  É vitoLLino com dois *LL's*
  
  
SUMÁRIO
--------

#. `IMPORTANDO O VITOLLINO`_
#. `IMPORTANDO MÓDULOS (SALAS)`_
#. `STYLE`_
#. `CENA`_
#. `SALA`_
#. `LABIRINTO`_
#. `ELEMENTO`_
#. `TEXTO (PopUp)`_
#. `BOTÃO`_
#. `MÚLTIPLA-ESCOLHA`_
#. `INVENTÁRIO`_
#. `MÚSICA`_
#. `CÓDIGO`_
#. `PORTAL`_
#. `DROPPER`_
#. `DROPPABLE`_


IMPORTANDO O VITOLLINO
-----------------------

Para utilizar os recursos do vitollino é necessário, primeiramente, importá-lo para o módulo que está trabalhando.

.. code:: python

    """É análogo ao caminho _spy/vitollino/main.py """
    from _spy.vitollino.main  import Classe_Desejada, Classe_Desejada2
   
Outra forma de também importar é:

.. code:: python

    """A abreviação do nome da classe pode auxiliar na organização e clareza do código posteriormente ;)"""
    from _spy.vitollino.main import  Classe_Desejada as abreviação_qualquer
    
IMPORTANDO MÓDULOS (SALAS)
---------------------------

.. code:: python

   """ Exemplo from cenas.imix import Inicial"""
    from  nome_do_pacote.nome_do_módulo import Classe_Desejada, funcao_Desejada
    
    
    
    """Essa linha impede cruzamentos indesejados entre os nomes dos repositórios."""
    if __name__ == "__main__":
        classe_principal()
    
    
.. seealso::
   
   Justificativa extensa da linha  `if __name__ == "__main__"`_

.. _if __name__ == "__main__": https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/


STYLE 
-------

O é utilizado para regular a altura e a largura da imagem que será mostrada.

.. code:: python
    
    from _spy.vitollino.main import STYLE
    
    
    STYLE["width"] = 900 # width = 300 (default) 
    STYLE["heigth"] = "900px" # min-height = "300px"


CENA
-----

A cena é uma tela com possibilidade de clique à esquerda,direita e centro.

.. code:: python

    from _spy.vitollino.main import Cena
    """Importa a classe Cena do Vitollino"""

    IMAGEM_QUALQUER = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_ESQUERDA = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_DIREITA = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_MEIO = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif

    nome_da_cena_direita = Cena(IMAGEM_DIREITA)
    nome_da_cena_esquerda = Cena(IMAGEM_ESQUERDA)
    nome_da_cena = Cena(IMAGEM_QUALQUER, # Parâmetro obrigatório
                    esquerda=nome_da_cena_esquerda, # default = NADA = SalaCenaNula()
                    direita=nome_da_cena_direita,  # default = NADA = SalaCenaNula()
                    meio=Cena(IMAGEM_MEIO)) # default = NADA = SalaCenaNula()
    nome_da_cena_esquerda.esquerda = nome_da_cena   
           
    nome_da_cena.vai()

SALA
-----

A sala é a formação de um ambiente formado de 4 cenas posicionadas em norte, sul, leste e oeste.

.. code:: python

    from _spy.vitollino.main import Cena, Sala
    """A Sala é uma COLEÇÃO de cenas organizadas nos pontos cadeais norte, sul, leste e oeste
    """


    IMAGEM_NORTE= "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_LESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_OESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_SUL = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif


    nome_da_cena_norte = Cena(IMAGEM_NORTE)
    nome_da_cena_sul = Cena(IMAGEM_SUL)
    nome_da_cena_leste = Cena(IMAGEM_LESTE)
    nome_da_cena_oeste = Cena(IMAGEM_OESTE)

    """ Bem como na composição na Cena, a ausencia de Cena em algum dos pontos cardeais direciona para a SalaCenaNula()"""
    nome_da_sala = Sala(n=nome_da_cena_norte, s=nome_da_cena_sul, l=nome_da_cena_leste, o=nome_da_cena_oeste)

    nome_da_sala.norte.vai() # A primeira Cena a ser visualizada
    #nome_da_sala.sul.vai()
    #nome_da_sala.leste.vai()
    #nome_da_sala.oeste.vai()

LABIRINTO
----------

O Labirinto é um conjunto de SALAS ligadas.

.. code:: python

   from _spy.vitollino.main import Cena, Sala, Labirinto
   """O Labirinto é uma coleção de Salas
   """

   IMAGEM_NORTE= "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM_LESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM_OESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM_SUL = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif

   IMAGEM2_NORTE= "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM2_LESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM2_OESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
   IMAGEM2_SUL = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif

   """Cria as cenas da primeira sala"""
   nome_da_cena1_norte = Cena(IMAGEM_NORTE)
   nome_da_cena1_sul = Cena(IMAGEM_SUL)
   nome_da_cena1_leste = Cena(IMAGEM_LESTE)
   nome_da_cena1_oeste = Cena(IMAGEM_OESTE)

   """Cria a sala com a primeira leva de cenas"""
   nome_da_sala1 = Sala(n=nome_da_cena_norte, s=nome_da_cena_sul, l=nome_da_cena_leste, o=nome_da_cena_oeste)

   """Cria as cenas da segunda sala"""
   nome_da_cena2_norte = Cena(IMAGEM2_NORTE)
   nome_da_cena2_sul = Cena(IMAGEM2_SUL)
   nome_da_cena2_leste = Cena(IMAGEM2_LESTE)
   nome_da_cena2_oeste = Cena(IMAGEM2_OESTE)

   """Cria a sala com as segunda leva de cenas"""
   nome_da_sala2 = Sala(n=nome_da_cena2_norte, s=nome_da_cena2_sul, l=nome_da_cena2_leste, o=nome_da_cena2_oeste)
   
   """Gera o Labirinto"""
   resulta_labirito=Labirinto(c=nome_da_sala1,n=nome_da_sala2)
   """Inicia o labirinto referenciando a Sala e a cena"""
   resulta_labirinto.centro.norte.vai()

ELEMENTO
---------

O elemento é um objeto estático colocado em alguma parte da cena. Pode ser inserido no inventário.

.. warning::

   Só é possível colocar elemento se houver alguma cena que acomode-a.

.. code:: python

   from _spy.vitollino.main import Cena, Elemento
   """ O elemento é um objeto passível de ser colocado em alguma cena.
   """
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   nome_da_cena = Cena(MINHA_CENA)
   nome_do_elemento = Elemento(MEU_ELEMENTO, tit="título_do_elemento", 
                              style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = nome_da_cena)

TEXTO (PopUp)
--------------

É uma mensagem que aparecerá na tela. 

* Texto associado a abertura da Cena

.. code:: python

   from _spy.vitollino.main import Cena, Elemento, Texto
   """ O objeto é o elemento clicável de alguma cena.
   """
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   nome_da_cena = Cena(FUNDO)
   nome_da_cena.vai()
   texto_ = Texto(nome_da_cena, txt = "Mensagem desejada")
   texto_.vai()


   
* Texto subordina aparecimento de Elemento

.. code:: python

   from _spy.vitollino.main import Cena, Elemento, Texto
   """ O objeto é o elemento clicável de alguma cena.
   """
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   def chama_elemento(*args):
       nome_do_elemento = Elemento(LIVRO, tit="título_do_elemento", 
                                   style=dict(height=60,widht=60, left=600, top=20)) # ou x=eixo_x, y=eixo_y, w=largura, h=altura
       nome_do_elemento.entra(nome_da_cena)   
   
   nome_da_cena = Cena(FUNDO)
   nome_da_cena.vai()
   texto_ = Texto(nome_da_cena, txt = "Mensagem desejada", foi = funcao_do_elemento) # o método foi() esconde o popup
   texto_.vai()
  

BOTÃO
------

O botão é um elemento visualizado como portal. Criando um botão é possível associar o clique a algum acontecimento.

Existe algumas formas de criar um botão:

* Associando ao método ``vai()`` da classe Elemento 

.. code:: python
   
   from _spy.vitollino.main import Cena, Elemento
   """ O botão é o elementoclicável de alguma cena.
   """
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   def funcao_de_acao_do_botao(event = None):
       #Funcao chamada no clique
       print("Você clicou no botão!") # evento associado ao clique: mensagem, cena, sala,módulo...   
       
   nome_da_cena = Cena(MINHA_CENA)
   nome_da_cena.vai() # instancia a cena 
   nome_do_elemento = Elemento(MEU_ELEMENTO, tit="título_do_elemento", 
                              style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = nome_da_cena,
                              vai = funcao_de_acao_do_botao)

   

* Associando ao evento do browser

.. code:: python
   
   from _spy.vitollino.main import Cena, Elemento, Texto
   """ O botão é o elemento clicável de alguma cena.
   """
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   def funcao_de_acao_do_botao(event = None):
       #Função chamada no clique resultará na chamada de um texto
       texto_surpresa = Texto(nome_da_cena, txt ="Mensagem que você deseja passar!")
       texto_surpresa.vai()
   
   nome_da_cena = Cena(MINHA_CENA)
   nome_da_cena.vai()
   nome_do_elemento = Elemento(MEU_ELEMENTO, tit="título_do_elemento", 
                              style=dict(height=60,widht=60, left=600, top=20), # ou x=eixo_x, y=eixo_y, w=largura, h=altura
                              cena = nome_da_cena)
                              
   nome_do_elemento.elt.bind("click", funcao_de_acao_do_botao)


MÚLTIPLA-ESCOLHA
-----------------

A múltipla escolha é implementada usando a classe Texto do Vitollino. Funciona como um popup onde o jogador pode selecionar algo (opção)

.. code:: python

   from _spy.vitollino.main import Cena, Texto
   """ A multipla escolha é um popup com opções
   """
   
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif

   def resultado(opcao_escolhida):
       # O novo popupque será gerado quando o foi() do texto forchamado
       dicionario = dict(A="Você clicou no A", B="Você clicou no B") # dicionário que guarda a devolutiva da opção escolhida
       devolutiva = Texto(nome_da_cena, txt=dicionario[opcao_escolhida])
       devolutiva.vai()   


   nome_da_cena = Cena(MINHA_CENA)
   nome_da_cena.vai()


   pergunta = Texto(nome_da_cena, txt = "Seu enunciado aqui", foi = resultado, A= "resposta", B= "resposta")
  pergunta.vai()
   

INVENTÁRIO
-----------

Inventário é um espaço onde os elementos encontrados podem ser guardados. Há dois modos de criar um inventário:

* Objeto **não** resgatável

.. code:: python

   from _spy.vitollino.main import Cena, Elemento
   from _spy.vitollino.main import INVENTARIO as inv
   """O inventário funciona como um depósito de elementos não resgatáveis
   """
   
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   
   
   inv.inicia() # comando que starta o inventário
   nome_da_cena = Cena(MINHA_CENA)
   nome_do_elemento = Elemento(MEU_ELEMENTO, tit="título_do_elemento", 
                              style=dict(height=60,widht=60, left=600, top=20), # ou ,x=eixo_x, y=eixo_y, w=largura, h=altura,
                              cena = nome_da_cena,
                              vai = self.coloca_no_inventario)
                              
   coloca_no_inventario = lambda *_: inv.bota(nome_do_elemento, True) #testar     
   
   def coloca_no_inventário(self, *_):
      """Gera um função que será resgatada no vai() do elemento para associar o clique à entrada no inventário"""
      inv.bota(nome_do_elemento, True)  
      
* Objeto Resgatável

É possível resgatar o Elemento construindo uma classe que tenha o método de resgate
     
.. code:: python

 from _spy.vitollino.main import Cena, Elemento
 from _spy.vitollino.main import INVENTARIO as inv
 
 MEU_ELEMENTO = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
 MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
 
 class Item_herdado(Elemento):
     """Construção de uma classe que herde de Elemento
     """
     def bota(self, *_): 
          """Aciona estado de inv.bota = True para que eventual clique devolva o Elemento para a cena"""
          inv.bota(self, True)
          #self.vai=lambda*_:self.resgata(x=x,y=y,w=w,h=h)
          """Método vai do Elemento atrelado ao evento de reposicionamento, onde o memento especifica os argumentos pedidos pelo método resgata."""
          self.vai=lambda*_:self.resgata(*self.memento)

      def resgata(self,x,y,w,h):
          """Método para resgate do Elemento no inventário"""
          self.x,self.y,self.w,self.h= x,y,w,h
          """Retira Elemento atrelado ao título do inventário"""
          inv.tira(self.tit)
          """Coloca Elemento na cena"""
          self.entra(inv.cena)
          """Aciona estado de inv.bota = False para que eventual clique devolva o Elemento para o inventário"""
          self.vai=self.bota

      def mementor(self,memento):
          """Permite que o style do elemento a ser recolocado na tela seja especificado"""
          self.memento=memento


  class Main():

      def __init__(self):
          inv.inicia()
          self.minha_cena=Cena(MINHA_CENA)

          self.meu_elemento=Item_herdado(MEU_ELEMENTO, tit="nome_do_meu_elemento",style=dict(height=60,widht=60, left=100, top=100),cena=self.minha_cena)
          self.meu_elemento.mementor((110,150,200,"200px"))
          self.meu_elemento.vai=self.meu_elemento.bota

          self.minha_cena.vai()

  if __name__ == "__main__":
      Main()     

MÚSICA
-------

.. code:: python

   from _spy.vitollino.main import Cena, Elemento
   
   MINHA_CENA = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
   MINHA_MUSICA = "string_correspondente_a_url_e_extensao_da_musica" # Extensões aceitas: mp3, mp4
   
   nome_da_cena = Cena(MINHA_CENA)
   nome_da_cena.vai()
   
   nome_da_musica = Musica(MINHA_MUSICA, loop = True, autoplay = True)

CÓDIGO
-------

PORTAL
--------

DROPPER
--------

DROPPABLE
----------

.. _Tutorial_Vitollino:

TUTORIAL VITOLLINO
===================
 
.. image:: _static/6_plataf_pacote.png

Acesse: `Documentação do Vitollino`_
------------------------------------

.. _Documentação do Vitollino: https://github.com/kwarwp/_spy/blob/master/vitollino/main.py

.. Warning:: 
  É vitoLLino com dois *LL's*
  
  
SUMÁRIO
--------

#. IMPORTANDO O VITOLLINO
#. IMPORTAÇÃO DE OUTRA SALA
#. STYLE
#. CENA
#. SALA
#. LABIRINTO
#. ELEMENTO
#. POPUP
#. TEXTO (PopUp)
#. CÓDIGO
#. BOTÃO
#. MÚLTIPLA-ESCOLHA
#. INVENTÁRIO
#. MÚSICA
#. PORTAL
#. DROPPER
#. DROPPABLE


IMPORTANDO O VITOLLINO
-----------------------

Para utilizar os recursos do vitollino é necessário importá-lo para o módulo em que está trabalhando.

.. seealso::

  Para saber mais sobre como os módulos e pacotes funcionam na plataforma veja: :ref: `Acessando o Salão Principal`

.. code:: python

    from _spy.vitollino.main  import Classe_Desejada, Classe_Desejada2
   
Outra forma de também importar é:

.. code:: python

    """Abreviações podem auxiliar na organização e clareza do código."""
    from _spy.vitollino.main import  Classe_Desejada as abreviação_qualquer
    
IMPORTANDO MÓDULOS (SALAS)
---------------------------

.. code:: python

    """ Exemplo:
         from  cenas.imix   import  Inicial
              pacote.módulo         classe
    """
    from  nome_do_principal.nome_do_módulo import Classe_Desejada, Classe_Desejada2
    .
    .
    .
    .
    .
    """Esta linha diferencia o main do módulo e o main do vitollino"""
    if __name__ == "__main__":
        Classe_do_Módulo_atual()

.. seealso::

   Justificativa extensa da linha  `if __name__ == "__main__":`_ 
 
.. _if __name__ == "__main__": : http://moodle.escolapiloto.peq.coppe.ufrj.br/mod/assign/view.php?id=299

STYLE 
-------

.. code:: python
    
    from _spy.vitollino.main import STYLE
    
    
    STYLE["width"] = 900 # width = 300 (default) 
    STYLE["heigth"] = "900px" # min-height = "300px"


CENA
-----

.. code:: python
    
    from _spy.vitollino.main import Cena
    """Importa a classe Cena do Vitollino"""
    
    IMAGEM_QUALQUER = "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_ESQUERDA = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_DIREITA = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_MEIO = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    
    nome_da_cena_meio = Cena(IMAGEM_MEIO) 
    nome_da_cena_direita = Cena(IMAGEM_DIREITA) 
    nome_da_cena_esquerda = Cena(IMAGEM_ESQUERDA) 
    nome_da_cena = Cena(IMAGEM_QUALQUER, # Parâmetro obrigatório
                        esquerda=nome_da_cena_esquerda, # default = NADA = SalaCenaNula()
                        direita=nome_da_cena_direita,  # default = NADA = SalaCenaNula()
                        meio=nome_da_cena_meio) # default = NADA = SalaCenaNula() 
                         )
    nome_da_cena.vai()

SALA
-----

.. code:: python
   
    from _spy.vitollino.main import Cena, Sala
    """Importa a classe Sala e Cena do vitollino.
       A Sala é uma COLEÇÃO de cenas organizados nos pontos cadeais norte, sul, leste e oeste 
    """
    
    
    IMAGEM_NORTE= "string_correspondente_a_url_e_extensao_da_imagem" # Extensões aceitas: png, jpg, jpeg e gif   
    IMAGEM_LESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_OESTE = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    IMAGEM_SUL = "string_correspondente_a_url_e_extensao_da_image" # Extensões aceitas: png, jpg, jpeg e gif
    
    
    nome_da_cena_norte = Cena(IMAGEM_NORTE) 
    nome_da_cena_sul = Cena(IMAGEM_SUL) 
    nome_da_cena_leste = Cena(IMAGEM_LESTE) 
    nome_da_cena_oeste = Cena(IMAGEM_OESTE)
    
    nome_da_sala = Sala(n=nome_da_cena_norte, s=nome_da_cena_sul, l=nome_da_cena_leste, o=nome_da_cena_oeste)
    """ Bem como na composição na Cena, a ausencia de Cena em algum dos pontos cardeais direciona para a SalaCenaNula()"""
    
    nome_da_sala.norte.vai() # A primeira Cena a ser visualizada
    #nome_da_sala.sul.vai()
    #nome_da_sala.leste.vai()
    #nome_da_sala.oeste.vai()


LABIRINTO
----------

ELEMENTO
---------

POPUP
-----

TEXTO (PopUp)
--------------

CÓDIGO
-------

BOTÃO
------

MÚLTIPLA-ESCOLHA
-----------------

INVENTÁRIO
-----------

MÚSICA
-------

PORTAL
--------

DROPPER
--------

DROPPABLE
----------


    

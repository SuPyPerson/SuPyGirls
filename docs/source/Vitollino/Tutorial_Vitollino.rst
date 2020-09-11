.. _Tutorial_Vitollino:

TUTORIAL VITOLLINO
===================
 
.. image:: _static/6_plataf_pacote.png

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
    from  nome_do_pacote.nome_do_módulo import Classe_Desejada, Classe_Desejada2

STYLE 
-------

.. code:: python
    
    from _spy.vitollino.main import STYLE
    .
    .
    .
    STYLE["width"] = 900 # width = 300 (default) 
    STYLE["heigth"] = "900px" # min-height = "300px"


CENA
-----

SALA
-----

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


    

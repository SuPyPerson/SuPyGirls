.. _Tutorial_Vitollino:



TUTORIAL VITOLLINO
===================
 
.. image:: _static/6_plataf_pacote.png

.. Warning:: 
  É vitoLLino com dois *LL's*
  
 Sumário
----------
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

.. code:: python

    """É análogo ao caminho _spy/vitollino/main
       Lê-se, lá na pasta _spy, tem uma pasta vitollino que carrega um tal de main. 
       Nesse main tem um Classe-Desejada. Separa esse último aí por favor! Vou usar.
    """
    from _spy.vitollino.main  import Classe_Desejada, Classe_Desejada2
   

Outra forma de também importar é:


.. code:: python

    """A abreviação do nome da classe pode auxiliar na organização e clareza do código posteriormente ;)"""
    from _spy.vitollino.main import  Classe_Desejada as abreviação_qualquer
    
IMPORTAÇÃO DE SALA MÓDYLOS 
--------------------------


STYLE 
-------

.. code:: python
    
    from _spy.vitollino.main import STYLE
    .
    .
    .
    STYLE["width"] = 900 # width = 300 (default) 
    STYLE["heigth"] = "900px" # min-height = "300px"


.. code:: python

    """A abreviação do nome da classe pode auxiliar na organização e clareza do código posteriormente ;)"""
    from _spy.vitollino.main import  Classe_Desejada as abreviação_qualquer

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


    

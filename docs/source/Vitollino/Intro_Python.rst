.. _Intro_Python:

Introdução ao Python
==========================

.. image:: _static/Python_Logo.png
    :height: 300px
    :width: 300px
    :align: center


.. Note:: 
   Este arquivo compreende uma fugaz introdução ao python.

Este documento pretende tornar familiar, à primeira vista, contextualizações importantes e sintaxes frequentes no uso linguagem. 

Espero que tão logo este documento seja parco frente à sua fome pythônica e você precise enfrentar o árduo plano das documentações :D

ÍNDICE
---------

*  `O que é Python?`_
*  `PROCEDURAL vs ORIENTADA A OBJETO`_
*  `Python: Sintaxe Básica`_  

 * `Variáveis`_
 * `Dados: Type e Id`_
    * `Booleans`_
    * `Integer e Float`_
    * `String`_
 * `Estrutura de Dados`_
   * `Lista`_
   * `Dicionário`_
   * `Tuplas`_
   * `String`_
   * `Set`_
 * `Operators`_
   * `Operadores aritméticos`_
   * `Operadores de atribuição`_
   * `Operadores de atribuição`_
   * `Operadores lógicos`_
   * `Operadores de identidade`_
   * `Operadores de associaçãos`_
 * `Funções`_
 * `Iterações: Loops`_
   * `If and Else `_
   * `While `_
   * `For`_
 * `Classe`_
 *  `Referências`_


O que é Python?
----------------

**Python é uma linguagem de programação! Tcharan!!!!!!**

Uma linguagem de programação de alto nível arquitetada para ser, simultâneamente, compreensível e poderosa! 

Criado por `Guido van Rossum`_ e lançado em 1991, a estura de controle (sintaxe) requerida pelo interpretador e a abordagem orientada a objeto auxiliam o programador a desenvolver códigos organizados e claros, sejam eles extensos ou breves.

Você pode ler mais sobre no `Python.org`_

PROCEDURAL vs ORIENTADA A OBJETO
==================================
    
O Paradigma da Programação
-----------------------------

O Paradigma é um conglomerado de classificações que são atribuídos às estruturas de código (sintaxe) que o programador utiliza.
Para ser mais claro, existem diversas linguagens de programação e também diversas formas de externalizar suas soluções através delas; estas soluções resultam em uma estrutura que pode ser classificada como um determinado paradigma.

Ahhhhhhh! Mas pra quê isso?

Bem, *isso* é resultado de um longo período de aprimoramento das linguagens de programação! Inicialmente a programação era difícil, requeria um graaande conhecimento, sobre a linguagem e computadores, e atenção do programador pois a escrita era de **baixo nível**, ou seja, eram compilados de instruções diretas para o computador ( Brinca um pouquinho aqui: `Código Binário`_ ). Tudo muito complexo, específico, engessado.


.. Note::
   Exemplo de linguagem baixo nível: Código Binário, Assembly

Com a caminhar da tecnologia as demandas passaram a ser outras! Muito trabalho para pouco programador e muita criatividade para linguagens que não conseguiam acompanhar!!

Daí surgem as linguagens de **alto nível**! As de terceira geração seguiam o paradigma procedural, e descreviam especificamente quais procedimentos utilizar para resolver o problema em específico. E mais uma vez tudo dependia do conhecimento profundo do desenvolvedor  e a programação ainda não era nada intuitiva.

.. Note::
   Exemplo de linguagem alto nível (Terceira Geração): COBOL,FORTRAN...

Observando, o nível da linguagem é dado de acordo com o grau de proximidade entre a estrura de programação e a estrutura da nossa língua! Nesse grupo estão as linguagens C, C++, JAVA, [...] e nosso amadinho PYTHON! 

Voltemos aos paradigmas...

Como dito, existem diversos paradigmas! Mas neste documento focaremos e dois: Programação Procedural e a Programação Orientada a Objeto.
   
Programação Procedural
-----------------------

Bem como o nome diz, se trata de uma programação centrada em procedimentos.
Este paradigma de programação apresenta-se comumente em blocos únicos, centrados na sequência, decisão e iteração (loops, condicionais...).

Flui bem em projetos breves. Já em projetos extensos a chance de uma única alteração descarrilhar toodo o programa é relevante!

Exemplo de código seguindo o paradigma procedural:

.. code :: python
   
    x,y = 3,4 # Determina variáveis
    w,h= 5,7  # Determina variáveis
    z = x+y   # Determina variável que representa a operação
    r = w+h   # Determina variável que representa a operação
    print("Esse é o valor de z:", z, "e esse é o valor de r:",r) # Retorno


Programação Orientada a Objeto (OO)
------------------------------------

.. seealso::
   Você pode ver outra explicação sobre OO aqui: :doc:`../intro_comp/PythonOO.rst` 

Bem como o nome diz, se trata de uma programação centrada nos objetos.
O objeto na OO é tudo aquilo que possui, conjuntamente, propriedades e operações.

Este paradigma de programação apresenta-se comumente em diversos blocos com comportamentos singulares e blocos de funcionamento conjunto. 
Diferente da programação procedural, a estrutura de um código orientado a objeto permite a solução de problemas pontuais e a adição ou subtração de novos comportamentos a qualquer momento, sem que a porção funcional do código sofra.  

Exemplo do código anterior seguindo o paradigma OO:

.. code:: python

    class Numeros(): 
        """Gera uma classe que permite operações numéricas
    
           :param val: Lista de números. -> int, float, complex  
        """
        def __init__(self, val):
            """ O __init__ é um método mágico do python que funciona como um consrutor.
                Toda vez que o Numeros() é chamado, o python cria um objeto e o passa como
                o primeiro parâmetro.
            """
            self.val = val 
            """Diz que o parâmetro self.val e análogo ao argumento que será atribuido na chamada da classe."""

        def opera_soma(val):
            """Método da classe Numeros() que se reserva da somas dos argumentos dados
            
               :param val: Lista de números. -> int, float, complex 
            """
            if isinstance(val,list):
                """A função isinstance() verifica se o valor dado é compatível com o Tipo de objeto requerido."""
               print(sum(val))
               """Se a verificação retorna 'True' segue para a operação."""
            else:
               """ Se a verificação retorna 'False' uma mensagem educada alertará o usuário."""
               print("Eu preciso de números para trabalhar! Me adianta aí!")
               
    """Chama o método opera_soma() da classe Numeros() para operar a lista"""
    Numeros.opera_soma([1,4,5,6]) #Lista de inteiros
    Numeros.opera_soma([1.3,1.5.1.6]) #Lista de floats
 
Python: Sintaxe Básica 
========================

Esta seção do documento busca seguir, evolutivamente, o paradigma de programação Orientado a Objeto.

.. Note::
  Os Tópicos abaixo, e outros mais aprofundados, podem ser encontradas na `Documentação Python`_ 

Variáveis
----------
.. code:: python

Dados: Type e Id
------------------
* Boolean
.. code:: python

* Integer e Float
.. code:: python

*String
.. code:: python

Estrutura de Dados
--------------------
* Lista
.. code:: python

* Dicionário
.. code:: python

* Tupla
.. code:: python

* String
.. code:: python

* Set
.. code:: python

Operators
-----------
* Operadores aritméticos
.. code:: python

* Operadores de atribuição
.. code:: python

* Operadores de comparação
.. code:: python

* Operadores lógicos
.. code:: python

* Operadores de identidade
.. code:: python

* Operadores de associação
.. code:: python

Funções
--------
.. code:: python

Iterações: Loops
----------------
* If and Else 
.. code:: python
* While 
.. code:: python
* For 
.. code:: python

Classe
--------
.. code:: python





Referências 
------------
#. `Paradigma da Programação`_
#. `Programação Procedural`_
#. `Programação Orientada a Objeto`_
#. `Linguagens de programação`_
#. `Métodos Mágicos`_

.. _Paradigma da Programação: https://pt.wikipedia.org/wiki/Paradigma_de_programa%C3%A7%C3%A3o
.. _Programação Orientada a Objeto: https://pt.wikipedia.org/wiki/Orienta%C3%A7%C3%A3o_a_objetos
.. _Programação Procedural: https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_procedural
.. _Linguagens de programação: https://www.treinaweb.com.br/blog/linguagens-e-paradigmas-de-programacao/
.. _Métodos Mágicos: https://www.python-course.eu/python3_magic_methods.php

.. _Python.org: https://www.python.org/doc/
.. _Guido van Rossum: https://en.wikipedia.org/wiki/Guido_van_Rossum
.. _Código Binário: https://www.invertexto.com/codigo-binario
.. _Documentação Python: https://docs.python.org/3/tutorial/index.html

Tutorial Vitollino
===================

Acesse aqui o :ref:`Tutorial_Vitollino` .

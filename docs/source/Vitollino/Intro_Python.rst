.. _Intro_Python:

**Introdução ao Python**
==========================

.. image:: _static/Python_Logo.png
    :height: 300px
    :width: 300px
    :align: center


.. Note:: 
   Este arquivo compreende uma fugaz introdução ao python.

Este documento pretende tornar familiar, à primeira vista, contextualizações importantes e sintaxes frequentes no uso linguagem. 

Espero que tão logo este documento seja parco frente a sua fome pythônica e você precise enfrentar o árduo plano das documentações :D

ÍNDICE
---------

*  `O que é Python?`_
*  `PROCEDURAL vs ORIENTADA A OBJETO`_
*  `Python: Sintaxe Básica`_  
 * `Variáveis`_
 * `Dados: Type e Id`_
    * `Booleans`
    * `Integer e Float`
    * `String`
 * `Estrutura de Dados`_
    * `Lista`
    * `Dicionário`
    * `Tuplas`
    * `String`
    * `Set`
 * `Operators`_
    * `Operadores aritméticos`
    * `Operadores de atribuição`
    * `Operadores de atribuição`
    * `Operadores lógicos`
    * `Operadores de identidade`
    * `Operadores de associaçãos`
 * `Funções`_
 * `Iterações: Loops`_
    * `If and Else`
    * `While`
    * `For`
 * `Classes`_
*  `Referências`_


O que é Python?
----------------

**Python é uma linguagem de programação! Tcharan!!!!!!**

Uma linguagem de programação de alto nível arquitetada para ser, simultâneamente, compreensível e poderosa! 

Criado por `Guido van Rossum`_ e lançado em 1991, a estura de controle (sintaxe) requerida pelo interpretador e a abordagem orientada a objeto auxiliam o programador a desenvolver códigos organizados e claros, sejam eles extensos ou breves.

Você pode ler mais sobre no `Python.org`_

**PARADIGMAS DE PROGRAMAÇÃO**
-------------------------------

O Paradigmas de programação são um conglomerado de classificações atribuidas às estruturas de código (sintaxe) que o programador utiliza.
Para ser mais claro, existem diversas linguagens de programação e também diversas formas de externalizar suas soluções através delas; estas soluções resultam em uma estrutura que pode ser classificada como um determinado paradigma.

Ahhhhhhh! Mas pra quê isso?

Bem, *isso* é resultado de um longo período de aprimoramento das linguagens de programação! Inicialmente a programação era difícil, requeria um graaande conhecimento, sobre a linguagem e computadores, e atenção do programador pois a escrita era de **baixo nível**, ou seja, eram compilados de instruções diretas para o computador ( Brinca um pouquinho aqui: `Código Binário`_ ). Tudo muito complexo, específico, engessado.


.. Note::
   Exemplo de linguagem baixo nível: Código Binário, Assembly

Com a caminhar da tecnologia as demandas passaram a ser outras! Muito trabalho para pouco programador e muita criatividade para linguagens que não conseguiam acompanhar!!

Daí surgem as linguagens de **alto nível**! As de terceira geração seguiam o paradigma procedural, e descreviam especificamente quais procedimentos utilizar para resolver o problema em específico. E mais uma vez tudo dependia do conhecimento profundo do desenvolvedor  e a programação ainda não era nada intuitiva.

.. Note::
   Exemplo de linguagem alto nível (Terceira Geração): COBOL,FORTRAN...

Observando, o nível da linguagem é dado de acordo com o grau de proximidade entre a estrutura de programação e a estrutura da nossa língua! Nesse grupo estão as linguagens C, C++, JAVA, [...] e nosso amadinho PYTHON! 

Voltemos aos paradigmas...

Como dito, existem diversos paradigmas! Mas neste documento focaremos em três: Programação Procedural, Programação Estruturada e a Programação Orientada a Objeto.
   
Programação Procedural
-----------------------

Bem como o nome diz, se trata de uma programação centrada em procedimentos.
Este paradigma de programação apresenta-se comumente em scripts corridos que determinavam, diretamente, as ações a serem tomadas pelo computador.

Exemplo de código seguindo o paradigma procedural na linguagem Assembly:

.. code:: python 
    
    lea si, string ; Atribui SI ao endereço de string.
    call printf    ; Coloca o endereço atual na pilha e chama o processo printf

    hlt            ; Encerra o computador.
    string db "Ola mundo!", 0

    printf PROC
        mov AL, [SI] ; Atribui à AL o valor no endereço SI.
        cmp AL, 0    ; Compara AL com nulo.
        je pfend     ; Pula se comparação der igual.

        mov AH, 0Eh
        int 10h      ; Executa uma função da BIOS que imprime o caractere em AL.
        inc SI       ; Incrementa em um o valor de SI.
        jmp printf   ; Pula para o início do processo.

        pfend:
        ret          ; Retorna para o endereço na posição atual da pilha.
   printf ENDP
    
Em python poderíamos conseguir o mesmo resultado:

.. code:: python
 
   print("Olá, Mundo!") #Teste aí no seu console! :D

Programação Estruturada
-----------------------

Bem como o nome diz, se trata de uma programação centrada na estrutura.
Este paradigma de programação apresenta-se comumente em blocos únicos, centrados na sequência, decisão e iteração (loops, condicionais...).

Flui bem em projetos breves. Já em projetos extensos a chance de uma única alteração descarrilhar toodo o programa é relevante!

Exemplo de código seguindo o paradigma estruturado:

.. code:: python
 
    def soma(*args):
        resultado = 0
        for numero  in args:
            resultado += numero
            print("Soma= ", resultado)
 
    soma(1,2,3)


Programação Orientada a Objeto (OO)
------------------------------------

.. seealso::
   Você pode ver outra explicação sobre OO aqui:  :doc:`../intro_comp/PythonOO`  

Bem como o nome diz, se trata de uma programação centrada nos objetos.
O objeto na OO é tudo aquilo que carrega, conjuntamente, propriedades e operações de uma classe. Quando 

Este paradigma de programação apresenta-se, comumente, em diversos blocos com comportamentos singulares, técnica denominada encapsulamento, e blocos de funcionamento conjunto. 

Diferente da programação procedural, a estrutura de um código orientado a objeto permite a solução de problemas pontuais e a adição ou subtração de novos comportamentos a qualquer momento, sem que a porção funcional do código sofra.  
Outro ganho no uso do paradigma OO é a reutilização do código (princípios de `HERANÇA`_ e `POLIMORFISMO`_) 

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
        def opera_soma_tambem(*args):
            #print(sum(args))
            return sum(args)
               
    """Chama o método opera_soma() da classe Numeros() para operar a lista"""
    Numeros.opera_soma([1.3,1.5,1.6])

    operacao_um = Numeros.opera_soma([1,4,5,6])  # objeto da classe Numeros
    print("O tipo do 'operacao_um' é:", type(operacao_um)) #NoneType
    
    """Chama o método opera_soma() da classe Numeros() para operar a tupla"""
    opera = Numeros.opera_soma_tambem(1,2,3,4)
    print("O tipo do 'opera' é:",type(opera)) #Type int
    
    """Determina Variável"""
    abacaxi = 5 #variável qualquer
    print("O tipo do 'abacaxi' é:",type(abacaxi)) #Type int
 
**Python: Sintaxe Básica** 
----------------------------

.. Note::
  Os Tópicos abaixo, e outros mais aprofundados, podem ser encontradas na `Documentação Python`_ 

Variáveis
----------
.. code:: python

   #Teste esse código no seu console
  
   nome_da_variavel = "valor da variavel"
   nome_da_outra_variavel = 5362543
   nome_da_outra_outa_variavel = [a,b,c,d,e,f,g,h]
   
   """Imprime na tela o valor da variavel"""
   print(nome_da_variavel)
   
Dados: Type e Id
------------------
* Boolean

.. code:: python
   
   """Booleano é um estado em python, composto de dois valores: Verdadeiro ou falso."""
   print(10 > 9)
   print(10 == 9)
   print(10 < 9)
   
* Inteiro,flutuante,complexo,string

.. code:: python

   #teste o código abaixo no seu console
   """ Numeros sem parte decimal recebem o tipo 'inteiro'(int) """
   inteiro_um = 12
   inteiro_dois = -45
   type(inteiro_um)
   
   """ Numeros com parte decimal recebem o tipo 'flutuante'(float) """
   flutuante_um = 12.4
   flutuante_dois = -45.6
   type(flutuante_um)
   
   """ Numeros com parte real e imaginnária recebem o tipo 'complex'"""
   complexo_um = 12+3j
   complexo_dois = 15-7j
   type(complexo_um)
   
   """ Tudo, TUDO MESMO, que está entres aspas é string no python"""
   string_um = "12+3j"
   string_dois = "Oi! Espero que esteja tudo bem aí!"
   type(string_um)
   
   """Tudo no python carrega uma identidade, um Id"""
   id(insira_uma_variavel_aqui) # substitua por alguma variável qualquer
   
Estrutura de Dados
--------------------

.. code:: python

   """ Tudo que está entres colchetes [] é lista no python"""
   lista_um = [1,2,3,[1,2,3[1,2,3]]] #quantas listas tem aqui dentro?
   lista_dois = ["oi",1,4.3,4+9j]
   type(lista_um)
   
   """ Tudo que tem uma chave e um valor é um dicionário no python"""
   dicionario_um = {"um":"1","dois":2,"cachorro":"buldog"} 
   type(dicionario_um["um"])
   type(dicionario_um["dois"])
   
   """ Valores entre parêntesis são uma tupla no python. Elas são imutáveis!"""
   tupla_um = (1,2,3,4,5) 
   type(tupla_um)
   
   """ Valores entre chaves são um conjunto (set) em python"""
   set_um = {1,2,3,4,"5","e ae"} 
   type(set_um)
  
Referências 
------------
#. `Paradigma da Programação`_
#. `Programação Procedural`_
#. `Programação Orientada a Objeto`_
#. `Linguagens de programação`_

#. `Variável`_
#. `Estrutura de Dado`_
#. `Operadores Python`_
#. `Função`_
#. `Classe`_


.. _Paradigma da Programação: https://pt.wikipedia.org/wiki/Paradigma_de_programa%C3%A7%C3%A3o
.. _Programação Orientada a Objeto: https://pt.wikipedia.org/wiki/Orienta%C3%A7%C3%A3o_a_objetos
.. _Programação Procedural: https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_procedural
.. _Linguagens de programação: https://www.treinaweb.com.br/blog/linguagens-e-paradigmas-de-programacao/
.. _Métodos Mágicos: https://www.python-course.eu/python3_magic_methods.php

.. _HERANÇA: https://www.treinaweb.com.br/blog/utilizando-heranca-no-python/
.. _POLIMORFISMO: https://professormarcolan.com.br/polimorfismo-em-python/


.. _Variável: https://www.devmedia.com.br/python-trabalhando-com-variaveis/38644
.. _Estrutura de Dado: https://docs.python.org/pt-br/3/tutorial/datastructures.html
.. _Operadores Python: https://www.w3schools.com/python/python_operators.asp
.. _Função: https://docs.python.org/pt-br/3.8/library/functions.html
.. _Classe: https://docs.python.org/3/tutorial/classes.html

.. _Python.org: https://www.python.org/doc/
.. _Guido van Rossum: https://en.wikipedia.org/wiki/Guido_van_Rossum
.. _Código Binário: https://www.invertexto.com/codigo-binario
.. _Documentação Python: https://docs.python.org/3/tutorial/index.html


:ref:`Tutorial Vitollino <Tutorial_Vitollino>`
-----------------------------------------------


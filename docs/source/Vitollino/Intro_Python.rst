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
*  `Paradigmas de Programação`_
*  `Python: Sintaxe Básica`_  
 * `Variáveis`_
 * `Espaço de nome`_
 * `Escopo`_ 
 * `Dados: Type e Id`_
    * `Boolean`
    * `Inteiro,flutuante,complexo,string`
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
 * `Iterações`_
    * `Condicionais`
    * `Loops`
 * `Funções`_    
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

   class Boneca():
        def __init__(self, cabelo, cor, roupa, modelo=""):
            self.modelo = modelo
            self.cabelo = cabelo
            self.cor = cor
            self.roupa = roupa

        def fala(self):
            # Codigo para a boneca falar

        def anda(self):
            # Codigo para a boneca andar
             
 
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

Espaço de nome
---------------
**"Os namespaces são uma ótima ideia - vamos fazer mais disso!"** - `The zen of python`_

Se imagine em uma sala de aula com mais 10 pessoas. 50% delas tem nome com grafia e sobrenomes idênticos e a outra metade são apenas idênticos na aparência. Seu trabalho é diferenciá-los. Qual seria sua estratégia?

O mesmO pode acontecer quando programamos. Dentro do nosso módulo é fácil criarmos um script sem nomes repetidos, porém, bem mais trabalhoso quando estamos usando módulos externos. 


Tudo no python (strings, listas, funções...) é um objeto, e todo objeto recebe um id equivalente tanto para o atributo quanto para a atribuição:

.. code:: python

  #teste o código abaixo no seu console
  Maria_Maia = 4 
  print('id(Maria_Maia) =', id(Maria_Maia)) # id 140071085578048

  Maria_Maia= Maria_Maia + 1
  print('id(Maria_Maia_plus_um) =', id(Maria_Maia)) # id 140071085578080
  print('id(5) =', id(5)) # id 140071085578080
    
  Josefa = 4
  print('id(Josefa) =', id(Josefa)) # id 140071085578048
  print('id(4) =', id(4)) # id 140071085578048
  
Para evitar conflitos o Python tem um sistema, nomeado **namespace**, para **garantir que todos os nomes atribuidos aos objetos (variáveis, funções, classes...) do programa sejam exclusivos**, evitando qualquer conflito. Quando você nomeia algum objeto, este passa a ser mapeado com o nome determinado, podendo, também, nomes diferentes mapearem o mesmo objeto ou nomes iguais mapearem objetos diferentes: 

.. code:: python

  #teste o código abaixo no seu console
  x = "Qual foi?" # namespace global
  def mostra_o_X_ai():
    x = "E aiiiiiiii!" #namespace local
    print(x)

  print(x) # Qual foi?
  mostra_o_X_ai() # E aiiiiiiii!
  
Olha que situação interessante! Para o Python o que determina qual 'X' deve ser apresentado é o **Escopo**;

Escopo
-------
O escopo do nome é o **local** onde determinada variável é acessível; sendo determinado pelo *bloco de instrução* a qual ele pertence.

.. code:: python
 
 #teste o código abaixo no seu console
 zero = 0 # Bloco de instrução 0; variável global
   um = 1 # Bloco de instrução 1; variável local
    dois = 2 # Bloco de instrução 2; variável local
     .
     .
     .
                     número_indefinido = inf # Bloco de instrução n; variável local
                      
O escopo de nome tem a função de classificar quais nomes de variáveis, funções e classes estão acessíveis em cada bloco de instrução. Quanto mais próximo de n está o escopo da variável requerida, mais restrito é o acesso a este objeto.
É importante ressaltar que cada variável é global internamente ao bloco que pertence, e local externamente ao bloco que pertence. Esta definição é O escopo é importante para expressão de hierarquias.


.. code:: python

    #teste o código abaixo no seu console
    VAR_GLOBAL="Bóson Treinamentos em Tecnologia"
    def escreve_texto():
        VAR_LOCAL="Fábio dos Reis"
        print("Variável global: ", VAR_GLOBAL)
        print("Variável local: ", VAR_LOCAL)
    print("Executando a função escreve_texto:")

    escreve_texto()

    print("Tentando acessar as variáveis diretamente:")
    print("Variável global: ", VAR_GLOBAL)
    print("Variável local: ", VAR_LOCAL) # Tentativa de chamar uma variável local como se fosse global

Fonte exemplo: `Bosontreinamentos`_

   
Dados: Type e Id
------------------
* Boolean

.. code:: python

   #teste o código abaixo no seu console
   """Booleano é um estado em python, composto de dois valores: Verdadeiro ou falso."""
   print(10 > 9) # True
   print(10 == 9) # False
   print(10 < 9) # False
   
* Inteiro,flutuante,complexo e string

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
   
   #teste o código abaixo no seu console
   
   """ Tudo que está entre colchetes [] é lista no python"""
   lista_um = [1,2,3,[1,2,3[1,2,3]]] #quantas listas tem aqui dentro?
   lista_dois = ["oi",1,4.3,4+9j]
   type(lista_um)
   
   """ Tudo que tem uma chave e um valor é um dicionário no python"""
   dicionario_um = {"um":"1","dois":2,"cachorro":"buldog"} 
   type(dicionario_um["um"])
   type(dicionario_um["dois"])
   
   """ Valores entre parêntesis () são uma tupla no python. Elas são imutáveis!"""
   tupla_um = (1,2,3,4,5) 
   type(tupla_um)
   
   """ Valores entre chaves {} são um conjunto (set) em python"""
   set_um = {1,2,3,4,"5","e ae"} 
   type(set_um)

Operadores
-----------
* Operadores aritméticos
.. code:: python

* Operadores de atribuição
.. code:: python

* Operadores lógicos
.. code:: python

* Operadores de identidade
.. code:: python

* Operadores de associaçãos
.. code:: python

Iterações
----------
Iterar é repetir algo.

* **CONDICIONAIS**

São estruturas que executam a **verificação** de estados com base nos argumentos passados.

As verificações são feitas pelos operadores condicionais que comparam os valores passados e retornam Verdadeiro ou Falso. 

+----------------+
|*SE* condição   |
|                |
|*ENTÃO* comando |
+----------------+

Veja alguns abaixo:

+----------------------------------------------------------------------------+
|                         **OPERADORES CONDICIONAIS**                        |
+===========+============+===================================================+
| *OPERADOR*|   *TIPO*   |                   *VALOR*                         |
+-----------+------------+---------------------------------------------------+
|    ==     |  Igualdade |     Verifica a igualdade entre dois valores.      |
+-----------+------------+---------------------------------------------------+
|    !=     | Igualdade  |     Verifica a diferença entre dois valores.      |
+-----------+------------+---------------------------------------------------+
|     >     | Comparação |   Verificar se o valor A é maior que o valor B.   |
+-----------+------------+---------------------------------------------------+
|     <     | Comparação |   Verifica se o valor A é menor que o valor B.    |
+-----------+------------+---------------------------------------------------+
|    >=     | Comparação | Verifica se o valor A é maior ou igual ao valor B.|
+-----------+------------+---------------------------------------------------+
|    <=     | Comparação | Verifica se o valor A é menor ou igual ao valor B.|
+-----------+------------+---------------------------------------------------+
|    In     | Seqüência  | Verifica se o valor A está contido em um conjunto.|
+-----------+------------+---------------------------------------------------+


A sintaxe de uma **condicional simples** é:

.. code:: python

   if operacao > valor_comparativo:
     print("operacao é maior que valor_comparativo") # Observe a identação!!
     
A sintaxe de uma **condicional composta** é:

.. code:: python

   if operacao > valor_comparativo:
     print("operacao é maior que valor_comparativo")
   else:
     print("operacao não é maior que valor_comparativo")
     
A sintaxe de uma **condicional aninhada** é:

.. code:: python

   if operacao > valor_comparativo:
     print("operacao é maior que valor_comparativo")
   elif operacao = valor_comparativo:
     print("operacao é igual que valor_comparativo") 
   else:
     print("operacao não é maior que valor_comparativo")
     
     
* **LOOP FOR**

Os Loops são laços de repetição (iterações) através de sequências (listas, tuplas, dicionários, conjuntos, strings...).

Com os loops é possível executar um conjuntos de instruções para cada item de um iterável.

Exemplos simples abaixo:

.. code:: python
 
   animais = ["leão", "macaco", "águia"]
   for x in animais:
       print(x)
       
.. code:: python
 
   for x in "paralelepipedo":
      print(x)
      
Declaração de quebra:

.. code:: python
   #Print x até quando x for macaco
   animais = ["leão", "macaco", "águia"]
   for x in animais:
       print(x) #leão, macaco
       if x == "macaco":
          break
          
.. code:: python
   
    # Pause o print de x quando x for macaco
    caco = ["leão", "macaco", "águia"]
    for x in caco:
        if x == "macaco":
           break
        print(x) #leão


Declaração de continuação:

.. code:: python

    caco = ["leão", "macaco", "águia"]
    for x in caco:
      if x == "macaco":
        continue
      print(x)

Listas aninhadas:

.. code:: python

    lista = [[1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14,15]]
    
   #print da lista
   for x in lista: 
       print(x)
       
    #print das listas aninhadas   
    for x in lista:
       for y in x:
         print(y)

Uso de funções:

.. code:: python

    for x in range(9):
      print(x)

* **LOOP WHILE**

.. code::

      i = 1
    while i < 6:
      print(i)
      if i == 3:
        break
      i += 1
  
Funções
---------
.. code:: python

Classes
---------
.. code:: python


Referências 
------------
#. `Paradigma da Programação`_
#. `Programação Procedural`_
#. `Programação Orientada a Objeto`_
#. `Linguagens de programação`_

#. `Variável`_
#. `Estrutura de Dado`_
#. `Operadores Python`_
#. `Condicionais Python`_
#. `Loop Python`_
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
.. _Condicionais Python: https://www.devmedia.com.br/aprendendo-a-programar-em-python-estruturas-condicionais-if/17358
.. _Loop Python: https://www.w3schools.com/python/python_for_loops.asp
.. _Função: https://docs.python.org/pt-br/3.8/library/functions.html
.. _Classe: https://docs.python.org/3/tutorial/classes.html

.. _Python.org: https://www.python.org/doc/
.. _Guido van Rossum: https://en.wikipedia.org/wiki/Guido_van_Rossum
.. _Código Binário: https://www.invertexto.com/codigo-binario
.. _Documentação Python: https://docs.python.org/3/tutorial/index.html
.. _The zen of python: https://wiki.python.org.br/TheZenOfPythonExplained
.. _Bosontreinamentos: http://www.bosontreinamentos.com.br/programacao-em-python/funcoes-em-python-escopos-de-variaveis/


:ref:`Tutorial Vitollino <Tutorial_Vitollino>`
-----------------------------------------------


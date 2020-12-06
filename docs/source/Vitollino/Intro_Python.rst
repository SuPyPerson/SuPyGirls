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
    * `Compreensão e Expressão Geradora`
      
      * `Compreensão de Listas`
      * `Compreensão de dicionários`
      * `Compreensão de Conjuntos`
      * `Expressão Geradora`
      
 * `Manipulação das Estruturas de dados`_

    * `Lista`
    * `Dicionário`
    * `Tuplas`
    * `String`
    * `Set`
    
 * `Built-in`_
 
    * `Zip`
    * `Slice`

 * `Operadores`_

    * `Operadores aritméticos`
    * `Operadores de atribuição`
    * `Operadores lógicos`
    * `Operadores de identidade`
    * `Operadores de Comparação`
    * `Operadores de Membro`

 * `Iterações`_

    * `Condicionais`
    * `Loops`

 * `Funções`_ 
 
   * Parâmetros Ordinais e Nomeados
   * Funções Anônimas/Lambda

 * `POO- Programação Orientado a Objeto`_

   * Herança
   * Polimorfismo
   
 * `Tópicos Avançados`_
 
   * Expressão Regular 

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
O objeto na OO é tudo aquilo que carrega, conjuntamente, propriedades e operações de uma classe. 

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
            
.. Tip:: 

   Você pode acessar o conteúdo de Programação Orientada Objeto acessando o tópico `POO- Programação Orientado a Objeto`_
 
 
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
   nome_da_outra_outra_variavel = [a,b,c,d,e,f,g,h]
   
   #decalração de múltiplas variáveis
   nome_da_variavel, nome_da_variavel_dois = "variavel_um", "variavel_dois"
   
   """Imprime na tela o valor da variavel"""
   print(nome_da_variavel)
   
         
.. Warning:: 
   
   É indicado não começar sua variável com:
   
   * número
  
   
.. Warning::

   **O python tem alguns nomes reservados:**
 
    ‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘async’, ‘await’, ‘break’, ‘class’, ‘continue’, 
    ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, 
    ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’

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
   
* Inteiro

.. code:: python

   #teste o código abaixo no seu console
   
   """ Numeros sem parte decimal recebem o tipo 'inteiro'(int) """
   inteiro_um = 12
   inteiro_dois = -45
   type(inteiro_um)

* Flutuante 

.. code:: python

   """ Numeros com parte decimal recebem o tipo 'flutuante'(float) """
   flutuante_um = 12.4
   flutuante_dois = -45.6
   type(flutuante_um)
   


* Complexo 

.. code:: python
   
   """ Numeros com parte real e imaginnária recebem o tipo 'complex'"""
   complexo_um = 12+3j
   complexo_dois = 15-7j
   type(complexo_um)
   

* String

.. code:: python
   
   """ Tudo, TUDO MESMO, que está entres aspas é string no python"""
   string_um = "12+3j"
   string_dois = "Oi! Espero que esteja tudo bem aí!"
   type(string_um)
   
   
   """Tudo no python carrega uma identidade, um Id"""
   id(insira_uma_variavel_aqui) # substitua por alguma variável qualquer
   
.. Tip::

   Quando estiver brincando com strings busque explorar os Metodos:
   
   * `join()`_
   * `translate()`_
   * `maketrans()`_
   * `upper()`_
   * `lower()`_
   * `strip()`_
   * `find()`_
   * `replace()`_

   
   
Estrutura de Dados
--------------------

* Lista

.. code:: python
   
   #teste o código abaixo no seu console
   
   """ Tudo que está entre colchetes [] é lista no python"""
   lista_vazia = []
   lista_um = [1,2,3,[1,2,3[1,2,3]]] #quantas listas tem aqui dentro?
   lista_dois = ["oi",1,4.3,4+9j]
   type(lista_um)

.. Tip::

   Quando estiver brincando com listas busque explorar os Metodos:
   

    * `len()`_
    * `index()`_
    * `append()`_
    * `extend()`_
    * `insert()`_
    * `remove()`_
    * `count()`_
    * `pop()`_
    * `reverse()`_
    * `sort()`_
    * `copy()`_
    * `clear()`_


* Dicionário


.. code:: python

   """ Tudo que tem uma chave e um valor é um dicionário no python"""
   dicionario_um = {"um":"1","dois":2,"cachorro":"buldog"} 
   dict_vazia = {}
   type(dicionario_um["um"])
   type(dicionario_um["dois"])
   
   dicionario_um.keys()
   decionario_um.values()
   
* Tupla

.. code:: python

   """ Valores entre parêntesis () são uma tupla no python. Elas são imutáveis!"""
   tupla_um = (1,2,3,4,5) 
   tupla_vazia = (,)
   type(tupla_um)
   
* Set

.. code:: python

   """ Valores entre chaves {} são um conjunto (set) em python"""
   set_um = {1,2,3,4,"5","e ae"} 
   type(set_um)
   
Manipulação das Estruturas de dados
------------------------------------

* Lista

* Tuplas

* String

* Set
   
*Compreensão e Expressão Geradora*
------------------------------------
 
Como dito anteriormente, o Python é uma linguagem poderosíssima! E alguns conceitos do python funcionam como atalhos na resolução de problemas computacionais.

Abaixo compilamos três funcionalidade muito poderosas da linguagem:

A compreensão é análoga a notação de conjuntos da matemática. Lembra?

    #. {x ^ 2: x é um número natural menor que 10}
    #. {x: x é um número inteiro menor que 20, x é ímpar}
    #. {x: x é uma letra na palavra ‘MATEMÁTICA’, x é uma vogal}
    
Exemplo: `Vooo-Insights`_

O tipo de compreensão dependerá do tipo de dado (Type) que você quererá como output.

* Compreensão de Listas
 
A compreensão de listas é utilizada onde, comumente, na busca por uma lista como output, usaríamos o loop.

Logo, onde antes nós faríamos:

.. code:: python

    lista = []
    for i in range(13):
        lista.append(i**2)

    print(lista)
    
Com a compreensão de lista conseguimos atribuir a construção da mesma lista da seguinte forma:

.. code:: python

    nueva_lista = [numero**2 for numero in range(13)]
    print(nueva_lista)

**A Sintaxe da compreensão de lista é:**

.. code:: python
 
    [expressão(variável) for variável in conjunto_input [predicate][, …]]
   

* Compreensão de dicionários

.. code:: python

* Compreensão de Conjuntos

.. code:: python

Built-in
----------

Os built-ins são funções integradas ao python prontinhas para uso!

Veja mais em: `BUILT-IN PYTHON.ORG`_

* Zip

A função `zip()` toma como argumento iteráveis (list, dict, string...) e as agrega a uma tupla.

Sintaxe da função:

.. code:: python

  zip(*iteravel)
  
Aplicação da função:
  
.. code:: python  

    #gerando as variáveis 
    lista_quantidade = [1, 2, 3]
    lista_alimentos = ['banana', 'laranja', 'maca']
    lista_qualidade =  ['estragado','maduro','verde']

    #nenhum iterável foi passado
    empty_zip = zip()
    print(empty_zip)
    # Converting iterator to list
    resultado_empty_list = list(empty_zip)
    print(resultado_empty_list)

    # Iteraveis passados
    lista_um = zip(lista_alimentos, lista_quantidade)
    lista_dois = zip(lista_alimentos, lista_quantidade,lista_qualidade)


    # Convertendo em conjunto de tuplas
    primeiro_zip= set(lista_um)
    segundo_zip = set(lista_dois)
    print(primeiro_zip)
    print(segundo_zip)
    
.. Tip::

   Os iteráveis passados podem não corresponder em quantidade!
   Teste no seu console:
   
   LISTA_GRANDE=['UM','DOIS','TRES','QUATRO']
   
   LISTA_PEQUENA = [1,2,3]
   

* Slice

A função `slice()` pode ser usado para fatiar obejtos sequenciais (strings, bytes, listas, tuplas, conjunto)...

Sintaxe da função:

.. code:: python

  slice(inicio, parar, pulo) 
  
  
Aplicação da função:

.. code:: python

    result1 = slice(1)
    print(result1) # default

    result2 = slice(1, 5, 2)
    print(slice(1, 5, 2))

    LISTA_GRANDE=['UM','DOIS','TRES','QUATRO','CINCO','SEIS']
 
    fatia_lista = slice(1) # corte no index 1
    #fatia_lista = slice(0,4) # corte do index 0 ao 4
    #fatia_lista = slice(0,-1,2) # corte do index 0 ao ultimo index pulando 2
    print(LISTA_GRANDE[fatia_lista])

Operadores
-----------

Os operadores python servem para designar **relações** entre as variáveis desejadas.

Veja alguns exemplos abaixo:


* Operadores aritméticos

+-------------------------------------------------------------------------------------------+
|                         **OPERADORES ARITIMÉTICOS**                                       |
+===========+===============+===============================================================+
| *OPERADOR*|     *TIPO*    |                   *VALOR*                         | *EXEMPLO* |
+-----------+---------------+---------------------------------------------------+-----------+
|     `+`   |     Adição    |          Realiza a soma entre dois valores.       |   10+7+4  |
+-----------+---------------+---------------------------------------------------+-----------+
|     `-`   |    Subtração  |      Realiza a subtração entre dois valores.      |  -10-7-4  |
+-----------+---------------+---------------------------------------------------+-----------+
|     `*`   | Multiplicação |     Realiza a multiplicação entre dois valores.   |    3*4    |
+-----------+---------------+---------------------------------------------------+-----------+
|     /     |    Divisão    |         Realiza a divisão entre dois valores.     |    10/5   |
+-----------+---------------+---------------------------------------------------+-----------+
|    //     |    Divisão    |         Retorna a parte inteira da divisão        |    10//5  |
+-----------+---------------+---------------------------------------------------+-----------+
|     %     |     resto     |    Retorna o resto da divisão entre dois valores. |    4%2    |
+-----------+---------------+---------------------------------------------------+-----------+
|    **     | Exponenciação | Multiplicação de um número por ele mesmo n vezes  |    4**2   |
+-----------+---------------+---------------------------------------------------+-----------+

.. code:: python

   # Teste esse código no seu console!
   n = 2
   z = 4

   a = n+z
   b = n-z
   c = n*z
   d = n/z
   e = n%z
   f = n**z

   print(a)


* Operadores de atribuição

Os Operadores de Atribuição Compostos realizam uma operação e em seguida, atribuem o resultado da operação para a
variável que está a esquerda do operador de atribuição.

+-------------------------------------------------------------------------------+
|                         **OPERADORES DE ATRIBUIÇÃO**                          |
+===========+===============+===================================================+
| *OPERADOR*|     *TIPO*    |                   *VALOR*                         |
+-----------+---------------+---------------------------------------------------+
|     =     |  igualdade    | Atribui à variável da esquerda o valor à direita  |
+-----------+---------------+---------------------------------------------------+
|     +=    |     Adição    |          Realiza a soma entre dois valores.       |
+-----------+---------------+---------------------------------------------------+
|     -=    |    Subtração  |      Realiza a subtração entre dois valores.      |
+-----------+---------------+---------------------------------------------------+
|     *=    | Multiplicação |     Realiza a multiplicação entre dois valores.   |
+-----------+---------------+---------------------------------------------------+
|     /=    |    Divisão    |         Realiza a divisão entre dois valores.     |
+-----------+---------------+---------------------------------------------------+
|     %=    |     Módulo    |    Retorna o resto da divisão entre dois valores. |
+-----------+---------------+---------------------------------------------------+
|    **     | Exponenciação | Multiplicação de um número por ele mesmo n vezes  |
+-----------+---------------+---------------------------------------------------+
|    &=     |               |                              Equivale a a = a & 8 |
+-----------+---------------+---------------------------------------------------+

.. code:: python

   # Teste esse código no seu console!
   n = 2
   z = 4

   n += z # resultado igual a 6
   n -= z # resultado igual a -2
   n *= z # resultado igual a 8
   n /= z
   n %= z
   n **= z

   print(a)

* Operadores lógicos

Os operadores lógicos unem expressões lógicas retornando um valor lógico binário compreendido entre não atendimento
da lógica (Falso) ou atendimento da lógica (Verdadeiro). Este tipo de dado (sim e não, zero e um, verdadeiro e falso) é
chamado `Booleano`_ e, no python, as constantes True e False são reconhecidas como pertencentes ao tipo de dado bool:

.. code:: python

   #Teste no seu console
   type(True) # <class 'bool'>
   type(False) # <class 'bool'>
   type(1 == 1) # <class 'bool'>


+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    **OPERADORES LÓGICOS**                                                                                                |
+===========+=================================================================+============================================================================+
| *OPERADOR*|                           *VALOR*                               |                           *RESULTADO*                                      |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     and   |        True se as duas expressões forem verdadeiras             | Se a primeira expressão é verdadeira, o resultado será a segunda expressão.|
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     or    |      False se, e somente se, duas expressões forem falsas       |Se a primeira expressão é falsa, o resultado seré a segunda expressão.      |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     not   | Muda o valor do argumento: not True é False, not False é True   |                                Booleano                                    |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     in    |           True se receber um o item a ser verificado            |                                Booleano                                    |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+

Combinações And:

+------+--------+------+
| AND  | False  | True |
+======+========+======+
| False|  False |False |
+------+--------+------+
| True | False  |True  |
+------+--------+------+

Combinações Or:

+------+--------+------+
| OR   | False  | True |
+======+========+======+
| False|  False |True  |
+------+--------+------+
| True | True   |True  |
+------+--------+------+

.. code:: python

    #Teste no seu console
    print("0 and 1:", bool(0 and 1))
    print(0 and 1)
    print("\n")
    
    print("1 and 0:", bool(1 and 0))
    print(1 and 0)
    print("\n")
    
    print("0 and 2:",bool(0 and 2))
    print(0 and 2)
    print("\n")
    
    print("2 and 0:",bool(2 and 0))
    print(2 and 0)
    print("\n")
    
    print("1 and 2:",bool(1 and 2))
    print(1 and 2)
    print("\n")
    
    print("3 and 2:",bool(3 and 2))
    print(2 and 3)
    print("\n")
    
    print("0 or 1:", bool(0 or 1))
    print(0 or 1)
    print("\n")
    
    print("0 or 0:", bool(0 or 0))
    print(0 or 0)
    print("\n")
    
    print("\n")
    print("not 0:", bool(not 0))
    print(not 0)
    
    print("\n")
    print("not 1:", bool(not 1))
    print(not 1)
    print("\n")

    print(2 in (2, 3)) # Saída True
    print(2 is 3) # Saída False
    
    
.. Note::

   #SyntaxWarning: "is" with a literal add ao python 3.8
   O compilador agora produz um SyntaxWarning quando as verificações de identidade (is e is not) são usadas com certos tipos de literais (por exemplo, strings,    
   números). Muitas vezes, eles podem funcionar por acidente no CPython, mas não são garantidos pela especificação da linguagem. 
   O aviso aconselha os usuários a usarem testes de igualdade (== e! =). (Contribuição de Serhiy Storchaka em bpo-34850.)

.. code:: python

    #Teste no seu console
    print('1. Idoso')
    print('2. Gestante')
    print('3. Cadeirante')
    print('4. Nenhum destes')
    resposta=int( input('Você é: ') )

    if (resposta==1) or (resposta==2) or (resposta==3) :
        print('Você tem direito a fila prioritária')
    else:
        print('Você não tem direito a nada. Vá pra fila e fique quieto')
        
Exemplo resgatado em `Python Progressivo`_

.. code:: python

    #Teste no seu console
    mes= input('Qual o mês?')
    dia_um= int(input('Que dia é hoje?'))
    dia_dois= int(input('Que dia é amanhã?'))

    if dia_um and dia_dois < 30 :
      print("Ainda estamos em", mes)
    else:
      print("Estamos próximos do próximo mês!")
      
      
.. code:: python

    int_x = int(input("Manda um inteiro aí!"))

    int_y = int(input("Manda outro aí!"))


    if (int_x == 10) or (int_y < 20):

        print("Uma das duas expressões é verdadeira!")

    else:

        print("Ambas são falsas!")


* Operadores de identidade

+---------------------------------------------------------------------------------------------------------------------+
|                                    **OPERADORES DE IDENTIDADE**                                                     |
+============+========================================================================================================+
| *OPERADOR* | *VALOR*                                                                                                |
+------------+--------------------------------------------------------------------------------------------------------+
| is         |  Retorna verdadeiro quando as variáveis são idênticas (referem-se ao mesmo objeto)                     |
+------------+--------------------------------------------------------------------------------------------------------+
| is not     | Retorna verdadeiro quando as variáveis nãp são idênticas (variáveis que não se referem ao mesmo objeto)|
+------------+--------------------------------------------------------------------------------------------------------+

.. code:: python

    #Teste esse código no seu console
    a = 3
    b = 3
    print(a is b) #True
    print(a is not b) #False

* Operadores de comparação

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    **OPERADORES COMPARATIVOS**                                                                                           |
+===========+=================================================================+============================================================================+
| *OPERADOR*|                           *VALOR*                               |                           *RESULTADO*                                      |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     >     |    True se o valor à esquerda é maior que o valor a direita     | Se a primeira expressão é verdadeira, o resultado será a segunda expressão.|
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     <     |      True se o valor à esquerda é menor que o valor a direita   | Se a primeira expressão é falsa, o resultado seré a segunda expressão.     |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     ==    | True se o valores à esquerda e a direita são equivalentes       |                               Booleano                                     |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     !=    |           True se o valor à esquerda é diferente ao da direita  |                    Booleano                                                |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     >=    | True se o valor à esquerda é maior ou igual ao da  direita      |                                Booleano                                    |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+
|     <=    | True se o valor à esquerda é menor ou igual ao da  direita      |                                Booleano                                    |
+-----------+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. code:: python

    #Teste esse código no seu console
    a = 3
    b = 3
    print(a>b) #True
    print(a==b) #False

* Operadores de Membro

+-----------------------------------------------------------------------------+
|                                    **OPERADORES DE MEMBROS**                |
+===========+=================================================================+
| *OPERADOR*|                           *VALOR*                               |
+-----------+-----------------------------------------------------------------+
|     in    |    True se o valor está contido do conjunto investigado         |
+-----------+-----------------------------------------------------------------+
| not in    |      True se o valor não está contido no conjunto investigado   |
+-----------+-----------------------------------------------------------------+

.. code:: python

    a = 10
    b = 2
    list = [1, 2, 3, 4, 5 ];

    if ( a in list ):
      print ("a - esta na lista")
    else:
      print ("a - não está na lista")

    if ( b not in list ):
      print ("b - não está na lista")
    else:
      print ("b - está na lista")

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

.. code:: python

      i = 1
    while i < 6:
      print(i)
      if i == 3:
        break
      i += 1
  
Funções
---------

Na programação a função é um bloco de código que realiza determinada tarefa que precisam ser executadas diversas vezes ou em momentos específicos.

A estrutura da função requer ``nome da função``, ``parâmetro`` e um ``corpo`` que representa o comportamento da função.

.. figure:: _static/Function_machine2.svg
   :scale: 50 %
   :align: center
   :alt: Estrutura da função.

* ``Nome da função``: É um nome arbitrário e será usado para **chamar** a função.
* ``parâmetro``: São os valores necessários para que o comportamento seja possível. O parâmetro pode ser uma lista, string, número... **dependerá** do comportamento esperado para a função.
* ``corpo``: Corpo é a instrução da função. É as ações que ela deverá tomar sobre os parâmetros parâmetros passados.

.. code:: python

   #estrutura da função
   def nome_da_função(parâmetro): # def é um termo reservado do python para dizer que é uma função
       corpo
       corpo
       corpo

.. Warning::

   Observe o `Escopo`_ do ``corpo`` da função. A *identação* é interna ao ``def``.  

Observe o exemplo de função abaixo:

.. code:: python
   
   # A função 'diga_o_nome' imprime sempre o nome que for digitado
   def diga_o_nome(nome): # 'diga_o_nome é o Nome da função; 'nome' é o parâmetro da função
       print(nome)        # função python print() é o corpo da função
       
   diga_o_nome("Gabriela") #observe como a função é chamada.
                           # "Gabriela" é o ARGUMENTO da função 'diga_o_nome'
                                                   
.. Note::

   Os parâmetros chamam-se ``parâmetro`` no cabeçalho da função. Quando chamamos a função, como em ``diga_o_nome_("Gabriela")``, o valor que fica dentro do parêntesis é chamado ``argumento``.
  
Você pode criar funções que não requerem parâmetros. Estas funções **sempre retornarão o mesmo resultado**.

.. code:: python
   
   # A função 'diga_o_nome' imprime sempre o nome que for digitado
   def diga_o_nome(): # 'diga_o_nome é o Nome da função
       nome = Gabriela    # observe que na ausência de parâmetros alguns valores precisam ser declarados
       print(nome)        # função python print() é o corpo da função
       
   diga_o_nome() #observe como a função é chamada
   
Como dito acima, as funções também são usadas quando determinados comportamento só deve ser chamado em horas oportunas. Observe o código abaixo:

.. Tip::

   Teste o código abaixo no seu console!

.. code:: python

    # Operação fora da função

    # o código:
    n1 = int(input('Chuta um número:'))
    n2 = int(input('Chuta mais um número'))
    soma = n1 + n2
    print("O resultado:", soma)

    # Mesma operação dentro da função
    def soma_FUN():
        n1 = int(input('Digite o Primeiro Número:'))
        n2 = int(input('Digite o Segundo Número:'))
        print("O resultado da função soma_FUN:", n1 + n2)

    soma_FUN()

Funções Anônimas/Lambda
-----------------

Uma forma mais *elegante* de programar é a construção de *funções lambda* ou *função anônima*.

A função lambda tem a seguinte sintaxe:
   
.. code:: python
   
   lambda argumentos da função: expressão/ação da função
   
Observe o exemplo abaixo:

.. code:: python

   dobro = lambda x: x*2
   print(dobro(5))


Parâmetros Ordinais e Nomeados
--------------------------------

Retomando, parâmetros são **valores** que serão utilizados pelo corpo da função para exercer alguns comportamentos. Quando a função não pede parâmetros, geralmente, as variáveis do corpo exercem tal função.

O parâmetros podem ser **ordinais** ou **nomeados**, ou seja, dependentes da posição ou do nome. Por exemplo:
centagem

.. code:: python
 
   # Uma função que calcula a porcentagem de um valor.
   def porcento(valor,porc=100):
       print(valor*(porc/100))
     
       
   porcento(100) # 100
   porcento(100,50) # 50

a função ``porcento`` pede: **parâmetro ordinal** ``valor`` e o **parâmetro nomeado** ``porc`` que, por ser nomeado, é o valor padrão/default da função, ou seja, sempre que chamarmos a função o argumento ``porc`` = ``100``

Vejamos um outro exemplo:

.. code:: python
 
   # Uma função que calcula descontos e porcentagens acumulativas.  
   def porcento_desconto(valor,descnt,porc=100):
       prctgm = valor*(porc/100) 
       print(int(prctgm-(prctgm*(descnt/100)))) # o int() é uma função python que retorna apenas os valores sem a casa decimal (inteiros).

       
   porcento_desconto(100) # TypeError: porcento() missing 1 required positional argument: 'descnt'
   porcento_desconto(100,0) # 100
   porcento_desconto(0,100) # 0 
   porcento_desconto(100,50) # 50
   porcento_desconto(100,50,50) # 25

.. Tip::

   Observe que no caso de **parâmetros ordinais** a ordem do chamado importa no resultado!!!!

Na função ``porcento`` pede: o **parâmetro ordinal** ``valor``, o **parâmetro ordinal** ``descnt``, e o **parâmetro nomeado** ``porc`` que torna ``100`` o valor padrão/default da função.

.. Warning::

   Todo **parâmetro ordinal** precisa ser passado no chamamento da função.
   
Veja alguns exemplos de funções python: `Funções Python`_

      
POO- Programação Orientado a Objeto
------------------------------------

**TUDO NO PYTHON É OBJETO!**

Grave esta frase. Retomaremos ela mais tarde.



Herança
--------

Polimorfismo
-------------

Tópicos Avançados
------------------

Bem-vindo a seção de tópicos avançados!

Não se assuste. Não é um espaço para tópicos difíceis, são apenas tópicos que requerem um conhecimento sólido sobre os tipos de dados e estruturas sintáticas que ele utiliza ;)

* Expressão Regular (RE)

A `expressão regular` corresponde a um módulo python que permite encontrar uma sequências, padrões, dentro de uma string.

Imagine um stencil com padrão `ABC`:

.. image:: _static/stencil.jpg

Agora imagine uma string como esta abaixo:

.. code:: python

    texto = """ fbusfGFHHFdhbsfhbsjfjjfgjjbFHFHFHFGHsahbdshdFHFGJFGJFGHFGHFHbsfgjgjsfjjsfD
                GhjshdvuvJfghfgjsgfgjfgjjjADABCHJFJFGFHFHHFHHgshfgjJdfhhHFHFHFGHFGsfghggDG
                FDGHJHGjhfhgHGFHJGFhgfhgfhgfHFHGHGChgchgchgcCHGHjhvhvhgCHGCHJGChgcjhgcJHGCH
            """
            
Como você faria para descobrir se o padrão do stencil `ABC` está na string `texto`?

Existem diversas formas: iterações, fatiamento de string e lista, built-in zip, etc. E há a expressão regular!

Ao utilizar o re a pergunta que queremos responder é: "Essa string corresponde a este padrão?" ou "Existealgum lugar nesta string que corresponda a este padrão?". O re também pode ser utilizados para manipular strings!

Antes de prosseguirmos deixe-me familiar você a alguns detalhes:

* METACARACTERES

Em sua grande maioria as letras e os caracteres correspondem a si mesmos. Por exemplo, a letra `a` corresponderá a qualquer letra `a` presente na string `"Eu fui à feira e não sabia o que comprar, sabia que havia esquecido a lista"` independente de ser o `a` que você procura! 

.. code:: python

    string = "Eu fui à feira e não sabia o que comprAr, sabia que havia esquecido a lista"
    stencil = "a"

    print(stencil in string, string.count(stencil)) #True, 9
    # Observe que a letra maiúscula foi ignorada pelo método count
    
Mas há descios a esta regra, O metacaracteres não correpondem a si mesmo mas sim a *marcadores* de exceções.

Os metacaracteres são os marcadores do seu stencil:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                         **METACARACTERES**                                                                                                                        |
+==============+==========================================================================+=========================================================================+
|*METACARACTER*|                                *VALOR*                                   |                                *EXPRESSÃO*                              |                                  
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    []        |  Especifica um conjunto unitarios de caracteres que você deseja combinar | `[ABC]`; `[A-E]`equivale a [ABCDE]; `[^ABC]` complementa excluindo o set|
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     .        | Corresponde a qualquer caracter única. Pode verificar a quantidade.      | `.`; `..`                                                               |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     ^        | Verifica se uma string **começa** com determinado conjunto de caracteres | `^A`; `^bE`                                                             |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     $        | Verifica se uma string **termina** com determinado conjunto de caracteres|`A$`; ^bE$`                                                              |           
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     *        | Verifica zero ou mais correspondências de uma ordem                      | `ma*n`                                                                  |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     +        | Verifica uma ou mais correspondências de uma ordem                       | `ma+n`                                                                  |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     ?        | Verifica zero ou uma correspondência de uma ordem                        |`ma?n`                                                                   |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    {}        | Verifica repetições em uma string                                        | `a{n,m}` onde n e m correspondem, respectivamente, o mínimo e o máximo  |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    ()        | Verifica subpadrões                                                      | `(a|b|c)xz` combina qualquer string que corresponda a abc seguida de xz |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \        | Esta folga é usada para "escapar" de caracteres e matacaracteres         | `\$` torna o matacaracter `$` em um caracter comum                      |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     |        | Verifica alternâncias                                                    | `a|a`                                                                   |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+

Algumas sequências especiais tornam alguns padrõesmais fáceis e escrever:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                         **SEQUENCIAS ESPECIAIS**                                                                                                                  |
+==============+==========================================================================+=========================================================================+
|*SEQ ESPECI*  |                                *VALOR*                                   |                                *EXPRESSÃO*                              |                                  
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    \A        | Verifica se uma string **começa** com determinado conjunto de caracteres | `\A`;                                                                   |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \b       | Corresponde aos caracteres que estão no início ou final                  | `\bKAKA` (início); `KAKA/b` (final)                                     |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \B       | É o oposto de \b                                                         | `\BKAKA` (início); `KAKA/B` (final)                                     |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \d       | Corresponde a qualquer dígito decimal. Equivale a [0-9]                  |`\d`;                                                                    |           
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \D       | Corresponde a qualquer dígito não decimal. Equivale a [^0-9]             | `\D`                                                                    |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \s       | Corresponde a uma string que contenha caracter de espaço e branco        | `\s`                                                                    |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \S       |          string que contenha qualquer caracter de espaço e branco que não| `\S`                                                                    |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    \w        | Verifica repetições em uma string                                        | `\w`                                                                    |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|    \W        | Verifica subpadrões                                                      | `\W`                                                                    |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
|     \Z       | Esta folga é usada para "escapar" de caracteres e matacaracteres         | `\$` torna o matacaracter `$` em um caracter comum                     |
+--------------+--------------------------------------------------------------------------+-------------------------------------------------------------------------+


Para utilizar os recursos do módulo RegEx, primeiramente você precisará importá-lo:

.. code:: python

    import re
    
posteriomente importar/colar seu texto 

.. code:: python

   import re
   
   minha_string = """blaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAbla
                  blaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblabla
                  blaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblabla
                  blaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblabla
                  blaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblablaBLAblabla
                  """
                  
Beleza! Agora precisará conhecer

Expressão Regular no doc python: `Doc_Python Re`_ 
            

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


.. _upper(): https://www.tutorialspoint.com/python/string_upper.htm
.. _lower(): https://www.w3schools.com/python/ref_string_lower.asp
.. _strip(): https://www.w3schools.com/python/ref_string_strip.asp
.. _find(): https://www.w3schools.com/python/ref_string_find.asp
.. _replace(): https://www.w3schools.com/python/ref_string_replace.asp
.. _join(): https://www.programiz.com/python-programming/methods/string/join
.. _translate(): https://www.programiz.com/python-programming/methods/string/translate
.. _maketrans(): https://www.programiz.com/python-programming/methods/string/maketrans


.. _pop(): https://www.tutorialspoint.com/python/list_pop.htm
.. _append(): https://www.programiz.com/python-programming/methods/list/append
.. _remove(): https://www.programiz.com/python-programming/methods/list/remove
.. _len(): https://www.programiz.com/python-programming/methods/built-in/len
.. _index(): https://www.programiz.com/python-programming/methods/list/index
.. _extend(): https://www.programiz.com/python-programming/methods/list/extend
.. _insert(): https://www.programiz.com/python-programming/methods/list/insert
.. _count(): https://www.programiz.com/python-programming/methods/list/count
.. _reverse(): https://www.programiz.com/python-programming/methods/list/reverse
.. _sort(): https://www.programiz.com/python-programming/methods/list/sort
.. _copy(): https://www.programiz.com/python-programming/methods/list/copy
.. _clear(): https://www.programiz.com/python-programming/methods/list/clear

.. _HERANÇA: https://www.treinaweb.com.br/blog/utilizando-heranca-no-python/
.. _POLIMORFISMO: https://professormarcolan.com.br/polimorfismo-em-python/
.. _Doc_Python Re:https://docs.python.org/3/howto/regex.html

.. _BUILT-IN PYTHON.ORG: https://docs.python.org/3/library/functions.html

.. _Variável: https://www.devmedia.com.br/python-trabalhando-com-variaveis/38644
.. _Estrutura de Dado: https://docs.python.org/pt-br/3/tutorial/datastructures.html
.. _Operadores Python: https://www.w3schools.com/python/python_operators.asp
.. _Condicionais Python: https://www.devmedia.com.br/aprendendo-a-programar-em-python-estruturas-condicionais-if/17358
.. _Booleano: https://pt.wikipedia.org/wiki/Boolean
.. _Loop Python: https://www.w3schools.com/python/python_for_loops.asp
.. _Função: https://docs.python.org/pt-br/3.8/library/functions.html
.. _Classe: https://docs.python.org/3/tutorial/classes.html

.. _Python.org: https://www.python.org/doc/
.. _Guido van Rossum: https://en.wikipedia.org/wiki/Guido_van_Rossum
.. _Código Binário: https://www.invertexto.com/codigo-binario
.. _Documentação Python: https://docs.python.org/3/tutorial/index.html
.. _The zen of python: https://wiki.python.org.br/TheZenOfPythonExplained
.. _Bosontreinamentos: http://www.bosontreinamentos.com.br/programacao-em-python/funcoes-em-python-escopos-de-variaveis/
.. _Python Progressivo: https://www.pythonprogressivo.net/2018/02/Operadores-logicos-AND-OR-NOT.html
.. _Funções Python: https://docs.python.org/pt-br/3/library/functions.html
.. _Vooo-Insights: https://www.vooo.pro/insights/tutorial-compreensao-de-listas-python-com-exemplos/

:ref:`Tutorial Vitollino <Tutorial_Vitollino>`
-----------------------------------------------

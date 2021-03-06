**INSTALAÇÃO DE SOFTWARES RECOMENDADOS**
=========================================

.. seealso::
   
   Este tutorial é uma adaptação do tutorial existente em: :doc:`../intro_comp/instalacao_programas`
   
SUMÁRIO
--------

#. `PYCHARM`_

   #. `INSTALAÇÃO DO PYCHARM`_
   #. `CONFIGURAÇÃO DO PYCHARM`_
   #. `IMPORTANDO PROJETOS`_
   #. `CLONANDO PROJETOS ATRAVÉS DO LINK`_
   #. `CLONANDO PROJETOS ATRAVÉS DA CONTA`_
   #. `IMPORTANDO BIBLIOTECAS NO PYCHARM`_

#. `SPYDER`_
#. `ANACONDA`_

 
PYCHARM
--------

PyCharm é um ambiente de desenvolvimento integrado (IDE) usado em programação de computadores , especificamente para a linguagem Python . É desenvolvido pela empresa checa JetBrains. Ele fornece análise de código, um depurador gráfico, um testador de unidade integrado, integração com sistemas de controle de versão (VCSes) e suporta desenvolvimento web com Django , bem como ciência de dados com Anaconda . [7] (Wikipedia, 2020)

INSTALAÇÃO DO PYCHARM
----------------------

1. Acesse o link `Download do Pycharm`_ 

.. image:: _static/P1.png

2. Escolha o download do ``Python Community``.

.. image:: _static/P2.png

3. Salve o arquivo no seu computador.

.. image:: _static/P3.png

4. Abra o arquivo que você baixou e clique em ``Next``.

.. image:: _static/P4.png

5. Selecione ``Next``

.. image:: _static/P6.png

6 Selecione todas as caixinhas e clique em ``Next``

.. image:: _static/P7.PNG

7. Selecione ``Install``

.. image:: _static/P8.png

8. Aguarde...

.. image:: _static/P9.png

9. Escolha ``reiniciar agora`` **ou** ``reiniciar depois`` e depois clique em ``finish``

.. Warning::

   Antes de selecionar ``Reboot now`` tenha certeza de que salvou todos os seus trabalhos!

.. image:: _static/P10.png


**Pronto!!!!! O Pycharm está instalado!**


CONFIGURAÇÃO DO PYCHARM
------------------------

10. Clique no ícone do Pycharm na sua área de trabalho.

.. image:: _static/confPC_1.png

11. Selecione ``Do not import settings`` e clique em ``ok``

.. image:: _static/P11.png

12. Selecione o tema que preferir:

.. image:: _static/P12.png

13. Selecione ``Skip Remaining and Set Defaults`` e **aguarde**:

.. image:: _static/P13.png

14. Após um tempo, o programa abrirá esta tela. Clique no ``configure``:

.. image:: _static/confPC_2.png

15. Clique em ``Settings``.

.. image:: _static/confPC_3.png

16. À esquerda, clique no ``>`` do ``Version Control`` e **depois** clique em ``Python Interpreter``.

Você verá esta tela:

.. image:: _static/confPC_4.png

17. Clique no espaço que diz ``<No interpreter>`` e selecione a opção ``Python 3.9``

**Antes**

.. image:: _static/confPC_5.png

**Depois**

.. image:: _static/confPC_6.png

.. Note::
   
   Esta etapa só foi possível pois instalamos previamente o python na máquina! :D

18. Agora clique em ``Apply`` e depois em ``ok``:

.. image:: _static/confPC_7.png


IMPORTANDO PROJETOS
---------------------

19. Você deve estar vendo esta tela agora:

.. image:: _static/confPC_8.png

20. Clique em ``Get from Version Control`` e **depois** em ``GitHub``

.. image:: _static/confPC_9.jpg

21. Nesta tela clique em ``Download and Install``. 

.. image:: _static/confPC_10.png

depois:

.. image:: _static/confPC_11.png


22. Nesta tela há duas possibilidades: *clonar projetos através do link* e *clonar projetos da conta github*

.. image:: _static/confPC_11.png

CLONANDO PROJETOS ATRAVÉS DO LINK
----------------------------------

1. Espere a conclusão do download do git.

.. image:: _static/confPC_11.png  
 
2. No espaço ``URL`` insira o link do repositório que você deseja clonar:

.. image:: _static/P14.png  

3. No espaço ``Directory`` dê um nome ao seu novo projeto (clone) alterando **a última parte do caminho**.

Exemplo:

.. code:: python
   
   C:\Users\DEV\PycharmProjects\NEW_PROJECT # este é o caminho atual
   
Eu posso alterar para:

.. code:: python
   
   C:\Users\DEV\PycharmProjects\Meu_Novo_Clone # este é o caminho com outro nome

.. Warnings::

   Não são aceitos **espaços**, logo, tudo deve estar unido por ``_``, ``-``
   
   Pontos ``.`` não são recomendados. 

4. Clique em ``Clone`` e verá esta tela:

.. image:: _static/P15.png  

5. Posteriormente verá esta:

.. image:: _static/P16.png  

6. E então **TCHARAAAAAM!!!!!**   Pycharm pronto para o uso!

.. image:: _static/P17.png  


CLONANDO PROJETOS ATRAVÉS DA CONTA
-----------------------------------

1. Clique no ``GitHub`` à esquerda.

.. image:: _static/confPC_11.png  

2. Clique em ``Log In via GitHub``

.. image:: _static/confPC_12.png  

3. Autorize o vículo entre o Pycharm e o GitHub

.. image:: _static/confPC_13.png  

4. Adicione seu login e senha

.. image:: _static/confPC_14.png  

5. Volte para o Pycharm e selecione o Repositório que deseja:

.. image:: _static/P18.png  

6. Aguarde o carregamento...

.. image:: _static/P15.png  

7. Posteriormente verá esta:

.. image:: _static/P16.png  

8. E então **TCHARAAAAAM!!!!!**   Pycharm pronto para o uso!

.. image:: _static/P17.png  

IMPORTANDO BIBLIOTECAS NO PYCHARM
----------------------------------

As bibliotecas são repositórios/módulos que guardam códigos que podem ser reutilizados posteriormente.

1. Abra algum projeto no Pycharm.

2. **Verifique se a biblioteca já está instalada** digitando ``import nome_da_biblioteca``

.. code:: python
   
   # vamos testar a existência da biblioteca matplotlib
   import matplotlib

.. image:: _static/DEP1.png  

3. Observando embaixo é possível ver a mensagem ``No module named matplotlib``, ou seja, o programa está reclamando que não há nenhum módulo instalado com esse nome.

.. image:: _static/DEP2.png  

4. Na barra superior clique em ``File`` e **depois** em ``settings``

.. image:: _static/DEP3.png  

5. Clique em ``Project: [...]`` e depois em ``Python Interpreter``

.. image:: _static/DEP4.png  

6. Clique no ``+`` ressaltado à direita

.. image:: _static/DEP4.png  

7. Escreva o nome da biblioteca que deseja no espaço:

.. image:: _static/DEP5.png  

8. Clique em ``Install Package`` na parte inferior da tela e aguarde (pode demorar)

.. image:: _static/DEP6.png  

8. A mensagem ``Package 'matplotlib' installed successfully`` confirma a instalação do pacote.

.. image:: _static/DEP7.png  

Feche as telinhas.

9. Voltando a tela inicial é possível observar que o console **não** reclama mais da ausência do módulo:

.. image:: _static/DEP8.png  

SPYDER
-------

ANACONDA
---------

.. _Download do Pycharm: https://www.jetbrains.com/pycharm/

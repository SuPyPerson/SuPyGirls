.. _acoes_entre_pycharm_github:


**AÇÕES ENTRE PYCHARM E GITHUB**
================================


SINCRONIZANDO  GITHUB E PYCHARM
-------------------------------

Abra o IDE Pycharm e prima > Check out from Version Control <



.. image:: _static/sincronizar1.jpg



Ao abrir as opções, prima > GitHub < para resgatar e logar na plataforma.



.. image:: _static/sincronizar2.jpg



Insira suas informações de usuário e prima >Login<

      **Atenção:**

            Host: github.com

            Auth Type: Password

.. image:: _static/sincronizar3.jpg

Na página seguinte, selecione o repositório do projeto >Git Repository URL<  e a “pasta pai” >Parent Directory<
-Veja Imagens- Feito isso, prima >Clone<

.. image:: _static/sincronizar4.jpg

Selecione o repositório a sua escolha

.. image:: _static/sincronizar5.jpg

Selecione a pasta "pai" de seu interesse.

.. image:: _static/sincronizar6.jpg

Abrirá um pop-up perguntando se você gostaria de abrio o diretório. Clique no sim.

.. image:: _static/sincronizar7.jpg

COMO ABRIR O PROJETO NO PYCHARM
-------------------------------

Observe o lado esquerdo do seu cursor e clique na primeira pasta.

.. image:: _static/abrir1.jpg

Clique com o botão direito sobre o projeto > New > Directory> src

.. image:: _static/abrir2.jpg

Clique com o botão direito sobre src> New > Python File > “main”

.. image:: _static/abrir3.jpg

Vai aprir um pop-uppedindo para você confirmar o novo arquivo. Diga ok.

.. image:: _static/abrir4.jpg

Surge a aba do novo arquivo em Python. Porem ela vai esta na cor vermelha.

.. image:: _static/abrir5.jpg

Para que seja realmente adicionado o arquivo, clique com o botão direito em src > git > +add

.. image:: _static/abrir6ok.jpg

Se o arquivo mudar de cor, ele está corretamente adicionado.

.. image:: _static/abrir7.jpg

CRIAR UM <BRANCH>
-----------------

Localize o nome de seu issue.

.. image:: _static/branch1.jpg

No pycharm, selecione o ícone setas > New Branch.

.. image:: _static/branch2.jpg

Nomeie seu Branch de forma a especificar o Issue que está trabalhando.

.. image:: _static/branch3.jpg

Na parte inferior da tela, aparecerá um balão dizendo que o branch foi criado.

.. image:: _static/branch4.jpg

COMMIT
------

Como enviar mudanças.


Após programar algo que é novo, descreva o seu código > selecione ‘commit’ > prima commit and push.

.. image:: _static/commit1.jpg


Aparecerá outra tela. Clique em push.

.. image:: _static/commit2.jpg

Pronto! Seu código foi enviado .

SALVAR MODIFICAÇÕES NA ORIGEM (MASTER)
--------------------------------------
Depois de enviar as últimas modificações. Abra o Github na aba code e dê um >Compare & Pull Request<

.. image:: _static/githubcompare&pull.jpg

Clique em create and pull request.

.. image:: _static/githubcreatpull.jpg

Aguarde o github acabar de checar

.. image:: _static/githubprocess.jpg

Clique em > Merge pull request<

.. image:: _static/githubmergeandpull.jpg

O seu pull request foi bem sucedido!

.. image:: _static/githubpullsucess.jpg

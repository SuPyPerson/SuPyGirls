<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <link rel="shortcut icon" href="image/favicon.ico" type="image/x-icon"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- stylesheets -->
    % for css in brython_css:
    <link rel="stylesheet" href="/css/{{ css }}.css" type="text/css"/>
    % end
    <!-- scripts -->
    % for scp in brython_js:
    <script type="text/javascript" src="/js/{{ scp  }}.js"></script>
    % end

    <script type="text/python">
            from browser import *
            from browser.local_storage import storage
            from _core.main import Main
            class MockBrython:
                document = document
                window = window
                html = html
                alert = alert
                storage = storage
                codename = "{{ pagetitle.replace(" - ", ".").lower() }}"
                code = """{{code}}"""
            main = Main(br=MockBrython)
            main.start()

    </script>

    <!--
    #! /usr/bin/env python
    # -*- coding: UTF8 -*-
    # Este arquivo é parte do programa Kwarwp
    # Copyright 2010-2018 Carlo Oliveira <carlo@nce.ufrj.br>,
    # `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
    #
    # Kwarwp é um software livre; você pode redistribuí-lo e/ou
    # modificá-lo dentro dos termos da Licença Pública Geral GNU como
    # publicada pela Fundação do Software Livre (FSF); na versão 2 da
    # Licença.
    #
    # Este programa é distribuído na esperança de que possa ser útil,
    # mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
    # a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
    # Licença Pública Geral GNU para maiores detalhes.
    #
    # Você deve ter recebido uma cópia da Licença Pública Geral GNU
    # junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

    """Brython front end client.

    .. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

    """

    -->
</head>
<body onLoad="brython({debug:1, cache:'browser', static_stdlib_import:true,
 pythonpath :['_spg','_spy/{{mod.replace("
", "_").lower()}}']})">
<!-- navigation -->
<div class="navigation">
    <nav class="nav has-shadow">
        <div class="container">
            <!-- nav site title -->
            <div class="nav-left">
                <a class="nav-item">
                    <h3 class="title is-3" style="color: white;">{{pagetitle}}</h3>
                </a>
            </div>
            <!-- end of site title -->

            <!-- this "nav-toggle" hamburger menu is only visible on mobile -->
            <span id="burg_menu" class="nav-toggle">
                % for item, name in menu:
	                <span><a class="nav-item is-tab" href="{{item}}">{{name}}</a></span>
                %end
            </span>
            <!-- end of toggle -->

            <!-- this "nav-menu" is hidden on mobile -->
            <div id="right_menu" class="nav-right nav-menu">
                % for name, item in menu:
                <a class="nav-item is-tab" href="{{item}}">
                    {{name}}
                </a>
                % end
            </div>
            <!-- end of nav -->
        </div>
    </nav>
</div>
<!-- end navigation -->
<!-- page content -->
<div class="main-content">
    <div class="container">
        <!-- start of about -->
        <div class="columns is-multiline is-centered">
            <!-- start of about -->
            <div class="column is-8">
                <div class="card">
                    <!-- about content -->
                    <div class="card-content">
                        <div class="content">
                            <div class="card-inner-wrapper">
                                <!-- about text -->
                                <div id="pydiv" class="card is-8by8" style="min-height:600px;">
                                    <figure>
                                        <img src="/image/{{image}}" width="1000px" alt="Image">
                                    </figure>
                                </div>
                                <!-- end of about text -->

                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- end of about column -->
        </div>
        <!-- end of about columns -->
    </div>
</div>
<!-- end of page content -->

<!-- footer: will stick to the bottom -->
<div class="footer footer-top-shadow">
    <div class="container has-text-centered">
	<span class="icon">
	  <i class="fa fa-github"></i>
	</span>
        <p>gaming platform by <a href="https://github.com/SuPyPerson/SuPyGirls">github.com/SuPyPerson/SuPyGirls</a></p>
        <p>this platform is proudly open source</p>
    </div>
</div>
<!-- end of footer -->
</body>
</html>

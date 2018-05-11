<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="/image/favicon.ico" type="image/x-icon"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- stylesheets -->
    % for css in brython_css:
    <link rel="stylesheet" href="/css/{{ css }}.css" type="text/css"/>
    % end
    <!-- scripts -->
    % for scp in brython_js:
    <script type="text/javascript" src="/js/{{ scp  }}.js"></script>
    % end
        <style>
            @keyframes fade {
                from {opacity: 1.0;}
                to {opacity: 0.0;}
            }
            .arena {  transform: translate(-50%, -50%);}
        </style>

    <script type="text/python">
            from browser import *
            from browser import ajax, timer
            from browser.local_storage import storage
            from _core.main import Main
            class MockBrython:
                document = document
                window = window
                html = html
                alert = alert
                ajax = ajax
                timer = timer
                storage = storage
                codename = "{{ pagetitle.replace(" - ", ".").lower() }}"
                code = """{{code}}"""
            main = Main(br=MockBrython)
            main.{{"play()" if pagetitle.startswith("PLAY - ") else "start()"}}

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
 pythonpath :['__code','__code/{{mod}}']})">
<!-- navigation -->
    % '' if pagetitle.startswith("PLAY - ") else include('menu.tpl')
<!-- end navigation -->
<!-- page content -->
<div class="main-content">
    <div class="container">
        <!-- start of about -->
        <div class="columns is-multiline is-centered">
            <!-- start of about -->
            <div class="column is-12">
                <div class="card">
                    <!-- about content -->
                    <div id="pydiv" class="card is-12by8" style="min-height:600px;">
                        <figure>
                            <img src="/image/{{image}}" width="1000px" alt="Image">
                        </figure>
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
    <div class="container">
        <!-- start of posts -->
        <div class="columns is-centered">
            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card-image">
                        <figure class="image is-4by1">
                            <a href="https://ufrj.br/">
                                <img src="/image/ufrj-logo-8.png"  alt="UFRJ">
                            </a>
                        </figure>
                    </div>
                    <!-- end of image for post -->
                </div>
            </div>
            <!-- end of post -->
            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card-image">
                        <figure class="image is-4by1">
                            <a href="http://www.nce.ufrj.br/">
                                <img src="/image/nce-logo-8.png" height="30px" alt="NCE">
                            </a>
                        </figure>
                    </div>
                    <!-- end of image for post -->
                </div>
            </div>
            <!-- end of post -->
            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card-image">
                        <figure class="image is-4by1">
                            <a href="http://labase.superpython.net/">
                                <img src="/image/labase-logo-8.png" height="30px" alt="LABASE">
                            </a>
                        </figure>
                    </div>
                    <!-- end of image for post -->
                </div>
            </div>
            <!-- end of post -->
            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card-image">
                        <figure class="image is-3by1">
                            <a href="http://www.sbc.org.br/2-uncategorised/1939-programa-superpython">
                                <img src="/image/sbc-logo-8.png" alt="SBC">
                            </a>
                        </figure>
                    </div>
                    <!-- end of image for post -->
                </div>
            </div>
            <!-- end of post -->
        </div>
        <!-- end of posts -->
    </div>
    <div class="container has-text-centered">


        <br>
        <p>gaming platform by <a href="http://www.superpython.net">www.superpython.net</a></p>
        <p>this platform is proudly open source</p>
    </div>
</div>
<!-- end of footer -->
</body>
</html>

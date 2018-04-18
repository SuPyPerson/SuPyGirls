<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <!-- stylesheets -->
    <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/css/bulma.css">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
    <link rel="shortcut icon" href="/image/favicon.ico" type="/image/x-icon"/>
</head>
<body>
<!-- navigation -->
<div class="navigation">
    <nav class="nav has-shadow">
        <div class="container">
            <!-- nav site title -->
            <div class="nav-left">
                <a class="nav-item">
                    <h3 class="title is-5" style="color: white;">SuperPython</h3>
                </a>
            </div>
            <!-- end of site title -->
            <div class="nav-middle">
                <a class="nav-item">
                    <h6 id="nav_saver" class="title is-6"
                        style="color: white; animation-name: fade; animation-duration: 4s;"></h6>
                </a>
            </div>

            <!-- this "nav-toggle" hamburger menu is only visible on mobile -->
            <span class="nav-toggle">
                <span><a class="nav-item is-tab" href="/site/help.html">Help</a></span>
                <span><a class="nav-item is-tab" href="/site/about.html">About</a></span>
                <span><a class="nav-item is-tab" href="/">Home</a></span>
	        </span>
            <!-- end of toggle -->

            <!-- this "nav-menu" is hidden on mobile -->
            <div class="nav-right nav-menu">
                <a class="nav-item is-tab" href="/site/help.html">
                    Help
                </a>
                <a class="nav-item is-tab" href="/site/about.html">
                    About
                </a>
                <a class="nav-item is-tab is-active" href="/">
                    Home
                </a>
            </div>
            <!-- end of nav -->
        </div>
    </nav>
</div>
<!-- end navigation -->

<!-- page header (title, etc) -->
<div class="main-header">
    <section class="hero">
        <div class="hero-body">
            <div class="container">
                <div class="has-text-centered">
                    <!-- header && subheader -->
                    <h1 class="title is-1 is-spaced">{{title.capitalize()}}</h1>
                    <h4 class="subtitle is-4">roll your own game with python</h4>
                    <!-- end of header && subheader -->

                </div>
            </div>
        </div>
    </section>
</div>
<!-- end page header -->

<!-- page content -->
<div class="main-content">
    <div class="container">
        <!-- start of posts -->
        <div class="columns is-multiline is-centered has-text-centered">
            % for count, scene in enumerate(cenas):
            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card is-2by2" style="height:114px; overflow:hidden;">
                        <figure>
                            <a href="/{{action.lower()+scene.lower().replace(' ','_')}}">
                                <img src="/image/{{image}}" width="1000px" alt="Image"
                                     style="position:relative; min-width:1200px;
                        top:{{'{}px'.format(-200 * (count // 6))}};
                       left:{{'{}px'.format(-200 * (count % 6))}};"></a>
                        </figure>
                    </div>
                    <!-- end of image for post -->

                    <!-- post header -->
                    <div class="card-content-header">
                        <h6 class="title is-6"><a href="/{{action.lower()+scene.lower()}}">{{scene}}</a></h6>
                    </div>
                </div>
            </div>
            <!-- end of post -->
            % end
        </div>
        <!-- end of posts -->
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

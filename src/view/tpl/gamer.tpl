<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <!-- stylesheets -->
    <link rel="stylesheet" href="/css/bulma.css">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
</head>
<body>
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
            <span class="nav-toggle">
	    <span></span>
	    <span></span>
	    <span></span>
	  </span>
            <!-- end of toggle -->

            <!-- this "nav-menu" is hidden on mobile -->
            <div class="nav-right nav-menu">
                <a class="nav-item is-tab is-active" href="/">
                    Home
                </a>
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
            <div class="column is-7">
                <div class="card">
                    <!-- about content -->
                    <div class="card-content">
                        <div class="content">
                            <div class="card-inner-wrapper">
                                <!-- about text -->
                                  <div class="card is-7by7"">
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

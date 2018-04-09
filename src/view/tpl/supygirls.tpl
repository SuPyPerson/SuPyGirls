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
      <link rel="shortcut icon" href="image/favicon.ico" type="image/x-icon"/>
  </head>
  <body>
    <!-- navigation -->
    <div class="navigation">
      <nav class="nav has-shadow">
	<div class="container">
	  <!-- nav site title -->
	  <div class="nav-left">
	    <a class="nav-item">
	      <h3 class="title is-3" style="color: white;">SuperPython</h3>
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
	    <a class="nav-item is-tab" href="/supygirls">
	      SuPyGirls
	    </a>
	    <a class="nav-item is-tab" href="/site/about.html">
	      About
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
                    <a href="/{{action.lower()+scene.lower()}}">
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

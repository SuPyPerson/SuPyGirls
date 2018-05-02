<nav class="navbar is-transparent">
  <div class="navbar-brand">
    <a class="navbar-item" href="http://www.superpython.net">
      <img src="/image/camisasuperpython.png" alt="Superpython" width="60" height="28">
    </a>
    <div id="burg_menu" class="navbar-burger burger" data-target="navbarExampleTransparentExample">
            <a class="navbar-item is-tab burger" href="#">

            </a>
            <a class="navbar-item is-tab burger" href="/site/help.html">
                Help
            </a>
            <a class="navbar-item is-tab burger" href="/site/about.html">
                About
            </a>
            <a class="navbar-item is-tab burger" href="/">
                Home
            </a>
    </div>
  </div>

  <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href="/supygirls/project">
        SuPyGirls
      </a>
      <a class="navbar-item" href="/supygirls/moduler/{{mod}}">
        {{modText}}
      </a>
      <a class="navbar-item" href="/supygirls/gamer/{{mod}}/{{nameText.lower()}}">
        {{nameText}}
      </a>
      <a class="navbar-item" href="/">
        <!--main.py-->
      </a>
      <a id="nav_saver"></a>
      <div id="nav_waiter" class="spinner">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
      </div>
    </div>

    <!-- this "nav-menu" is hidden on mobile -->
    <div id="right_menu" class="navbar-end">
        % for name, item in menu:
        <a class="navbar-item is-tab" href="{{item}}">
            {{name}}
        </a>
        % end

    </div>
    <!-- end of nav -->
  </div>
</nav>


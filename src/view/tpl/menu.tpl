<nav class="navbar is-transparent">
  <div class="navbar-brand">
    <a class="navbar-item" href="http://www.superpython.net">
      <img src="/image/camisasuperpython.png" alt="Superpython" width="60" height="28">
    </a>
      <a class="navbar-item" href="/supygirls/project">
        SuPyGirls
      </a>
      <a class="navbar-item" href="/supygirls/moduler/{{mod}}">
        {{modText}}
      </a>
      <a class="navbar-item" href="/supygirls/gamer/{{mod}}/{{nameText.lower()}}">
        {{nameText}}
      </a>
      <a id="nav_saver"></a>
      <div id="nav_waiter" class="spinner">
          <div class="bounce1"></div>
          <div class="bounce2"></div>
          <div class="bounce3"></div>
      </div>
    <span class="navbar-burger" data-target="navbar-menu">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </span>
  </div>

  <div id="navbar-menu" class="navbar-menu">
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


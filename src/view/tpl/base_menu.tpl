<div class="navbar">
   <nav class="nav has-shadow" role="navigation" aria-label="dropdown navigation">
        <div class="container">
            <!-- nav site title -->
            <div class="navbar-start">
                <a class="navbar-item">
                    <h3 class="title is-5" style="color: white;">{{pagetitle}}</h3>
                </a>
            </div>
            <!-- end of site title -->

            <!-- this "nav-toggle" hamburger menu is only visible on mobile -->
            <span id="burg_menu" class="navbar-burger">
	                <span><a class="navbar-item is-tab" href="#">|&nbsp;|</a></span>
                % for item, name in menu:
	                <span><a class="navbar-item is-tab" href="{{item}}">{{name}}</a></span>
                %end
            </span>
            <!-- end of toggle -->

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
</div>


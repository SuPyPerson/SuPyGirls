<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{pagetitle}}</title>
    <!-- stylesheets -->
    <meta http-equiv="content-type" content="application/xml;charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/css/bulma.css">
    <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
    <!-- fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
    <link rel="shortcut icon" href="/image/favicon.ico" type="/image/x-icon"/>
    <script type="text/javascript">
        function claim_project(project, autor){
            if (autor != 'livre') { return true;}
            var MODAL = document.getElementById("ident-modal");
            var FORM = document.getElementById("ident-form");
            
            var currentClass = MODAL.className;
            if (currentClass == "modal") { // Check the current class name
                MODAL.className = "modal is-active";   // Set other class name
                FORM.action = "/supygirls/__claim/{{claim}}" + project + "/"
            } else {
                MODAL.className = "modal";  // Otherwise, use `second_name`
            }
        }   
    </script>
</head>
<body>
<!-- navigation -->
    % include('base_menu.tpl')
<!-- end navigation -->
<!-- modal for user identification -->
    % include('form.tpl')
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
            % for count, (scene, author) in enumerate(cenas):
                <%
                    is_livre = 'onclick="claim_project('+"'{}'".format(scene.lower()+');"')
                    not_is_livre = 'href={}{}'.format(action.lower(),scene.lower())
                %>

            <!-- start of post -->
            <div class="column is-2">
                <div class="card">
                    <!-- image for post -->
                    <div class="card is-2by2" style="height:114px; overflow:hidden;">
                        <figure>
                            <a href="{{action.lower()+scene.lower().replace(' ','_')}}">
                                <img src="/image/{{image}}" width="1000px" alt="Image"
                                     style="position:relative; min-width:1200px;
                        top:{{'{}px'.format(-200 * (count // 6))}};
                       left:{{'{}px'.format(-200 * (count % 6))}};"></a>
                        </figure>
                    </div>
                    <!-- end of image for post -->

                    <!-- post header -->
                    <div class="card-content-header">
                        <!--h6 class="title is-6"><a href="/{{action.lower()+scene.lower()}}">{{scene}}</a></h6-->
                        <h5 class="title is-5"><a  href="{{action.lower()+scene.lower()}}">{{scene}}</a></h5>
                        <a class="subtitle is-6" onclick="claim_project('{{scene.lower()}}', '{{author}}');">{{author}}</a>
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

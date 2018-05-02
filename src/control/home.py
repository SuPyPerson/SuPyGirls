import os.path

from bottle import run, TEMPLATE_PATH, static_file, route, default_app

from . import tpl_dir
from . import py_dir
from . import static_controller
from . import game_controller
from . import code_controller
from . import play_controller
from . import supygirls_controller

# Create a new list with absolute paths
# TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))
# make sure the default templates directory is known to Bottle

if tpl_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, tpl_dir)


@route('/')
def index():
    return static_file('index.html', root=tpl_dir)


@route('/kwarwp')
def kwarwp():
    return static_file('kwarwp.html', root=tpl_dir)


application = default_app()
_ = application

# Mount a new instance of bottle for each controller and URL prefix.
# appbottle.mount("/external/brython/Lib/site-packages", project_controller.bottle)
# application.mount("/<:re:.*>/_spy", code_controller.bottle)
application.mount("/<:re:.*>/stlib", static_controller.appbottle)
application.mount("/<:re:.*>/image", static_controller.appbottle)
application.mount("/<:re:.*>/css", static_controller.appbottle)
application.mount("/<:re:.*>/site", static_controller.appbottle)
application.mount("/<:re:.*>/edit", game_controller.appbottle)
application.mount("/<:re:.*>/game/", game_controller.appbottle)
application.mount("/<:re:.*>/game/<:re:.*>/__code/", code_controller.appbottle)
# application.mount("/<:path>/__code/", code_controller.appbottle)
application.mount("/<:re:.*>/play/", play_controller.appbottle)
application.mount("/<:re:.*>/supygirls/", supygirls_controller.appbottle)

if __name__ == "__main__":
    run(host='localhost', port=8080)

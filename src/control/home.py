from bottle import get, run, view, TEMPLATE_PATH, Bottle, static_file
import os.path
from . import code_controller
from . import static_controller
from . import py_dir

# Create a new list with absolute paths
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))

application = Bottle()
_ = application

# Mount a new instance of bottle for each controller and URL prefix.
# appbottle.mount("/external/brython/Lib/site-packages", project_controller.bottle)
# application.mount("/<:re:.*>/_spy", code_controller.bottle)
application.mount("/<:re:.*>/stlib", static_controller.appbottle)
application.mount("/<:re:.*>/image", static_controller.appbottle)
application.mount("/<:re:.*>/css", static_controller.appbottle)
application.mount("/<:re:.*>/site", static_controller.appbottle)


@get('/supygirls')
@view("supygirls")
def index():
    return dict(mod='a0')


# Static Routes
@get("/_spy/_core/<filepath:re:.*\.py>")
def py(filepath):
    print("py(filepath):", filepath, py_dir)
    return static_file(filepath, root=py_dir)


if __name__ == "__main__":
    run(host='localhost', port=8080)

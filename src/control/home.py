from bottle import get, run, view, TEMPLATE_PATH
import os.path

# Create a new list with absolute paths
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))


@get('/')
@view("home")
def index():
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))
    return {}


run(host='localhost', port=8080)

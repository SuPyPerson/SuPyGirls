from bottle import get, run, view, TEMPLATE_PATH, Bottle
import os.path

# Create a new list with absolute paths
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))

application = Bottle()


@get('/')
@view("index")
def index():
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../view/tpl')))
    return {}


if __name__ == "__main__":
    run(host='localhost', port=8080)

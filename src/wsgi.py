from control.home import application
import bottle
import os
project_server = os.path.dirname(os.path.abspath(__file__))
tpl_dir = os.path.join(project_server, 'view/tpl')

_ = application


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root=tpl_dir)


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)

from control.home import application
import bottle
import os
import sys
project_home = os.path.dirname(os.path.abspath(__file__))

# add your project directory to the sys.path
# project_home = u'/home/supygirls/dev/SuPyGirls/src'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from control.home import application
# from bottle_app import application

_ = application


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080)

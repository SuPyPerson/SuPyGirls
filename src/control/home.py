import os.path

from bottle import get, run, view, TEMPLATE_PATH, Bottle, static_file

from . import py_dir
from . import static_controller

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
CENAS = ["{}".format(chr(a)) for a in range(ord('a'), ord('z') + 1) if chr(a) not in 'aeiouy']
GIRLS = ['Roxanne', 'Stacy-Marie', 'Libby', 'Sara', 'Kellee', 'Courtney', 'Angie', 'Parisa', 'Natalia', 'Kathryn',
         'Callie', 'Lisa', 'Ruzwana', 'Naomi', 'Tracy', 'Morgan', 'Rachel', 'Soraya', 'Amanda', 'Alexa', 'Julia',
         'Sarah', 'Heather', 'Adda', 'Samantha', 'Kristen', 'Anastasia', 'Meredith', 'Danae', 'Grace']
CGIRLS = ['Ada', 'Henrietta', 'Grete', 'Gertrude', 'Betty', 'Hedy', 'Kathleen', 'Grace', 'Mary Shaw', 'Evelyn', 'Ida',
          'Mary Klawe', 'Dana', 'Jean', 'Dame', 'Joan', 'Sister Mary', 'Margaret', 'Vera', 'Margaret Hamilton', 'Erna',
          'Margaret Fox', 'Mary Lou', 'Adele', 'Karen', 'Sandra', 'Susan Nycum', 'Phyllis', 'Elizabeth', 'Irene',
          'Sophie', 'Patricia', 'Carol', 'Carla', 'Lorinda', 'Janese', 'Roberta', 'Susan Kare', 'Radia', 'Irma',
          'Monica', 'Eva', 'Frances Allen', 'Donna', 'Shafi', 'Barbara', 'Sally', 'Xiaoyuan', 'Anita',
          'Mary Coombs', 'Ellen', 'Jeri', 'Lucy', 'Audrey', 'Maria', 'Melanie', 'Joanna', 'Megan', 'Sarah', 'Kesha']


@get('/supygirls')
@view("supygirls")
def project():
    return dict(pagetitle="SuPyGirls", action="supyg/", title="SUPYGIRLS", image="miro.jpg", cenas=CGIRLS)


@get('/supyg/<name>')
@view("supygirls")
def moduler(name):
    return dict(
        pagetitle="SuPyGirls - {}".format(name), title=name, action="game/{}/".format(name),
        image="garden.jpg", cenas=GIRLS)


@get('/game/<mod>/<name>')
@view("gamer")
def gamer(mod, name):
    return dict(pagetitle="SuPyGirls - {} - {}".format(mod, name), title=name, image="supygirls_logo.png")


# Static Routes
@get("/_spy/_core/<filepath:re:.*\.py>")
def py(filepath):
    print("py(filepath):", filepath, py_dir)
    return static_file(filepath, root=py_dir)


if __name__ == "__main__":
    run(host='localhost', port=8080)

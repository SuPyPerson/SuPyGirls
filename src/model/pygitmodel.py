from github import Github
import os.path
import os as op

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPackage/SuPyGirls.git"
USERNAME = "carlotolla"
PASSWORD = op.environ["ISME"]

g = Github(USERNAME, PASSWORD)
u = g.get_user()
r = None
for repo in u.get_repos():
    if "SuPyGirls" in str(repo.name):
        r = repo
        break
    print(type(repo.name), repo.name)

rp = u.get_repo("supyjogo")  # "activlets")

print(r)
[print(org) for org in rp.get_branches()]
al = rp.get_branch("uva")
cm = al.commit

print(al.etag, al.commit.sha)
print("cont", rp.get_file_contents("/uva/main.py", cm.sha).decoded_content)


class Project:
    """
    Contains a collection of packages to be assigned to each user
    """
    key = ""

    @classmethod
    def get(cls, name):
        """
        Find a project with a given name.
        
        :param name: project name to be found.
        :return: the project retrieved or None if not found.
        """
        return cls if name else None

    @classmethod
    def create(cls, name, sprite, content=None):
        return cls if name and sprite and content else None

    @classmethod
    def ismember(cls, project, person):
        pass

    @classmethod
    def islogged(cls, person):
        pass

    @classmethod
    def removesession(cls, person):
        pass


class Package:
    """
    Contains a collection of modules developed by each user
    """

    @classmethod
    def get(cls, name):
        """
        Find a package with a given name.
        
        :param name: package name to be found.
        :return: the package retrieved or None if not found.
        """
        return cls if name else None

    @classmethod
    def create(cls, project, name, content=None):
        return cls if project and name and content else None


class Module:
    """
    A module developed by a user
    """
    content = ""

    @classmethod
    def get(cls, name):
        """
        Find a module with a given name.
        
        :param name: package name to be found.
        :return: the package retrieved or None if not found.
        """
        return cls if name else None

    @classmethod
    def obtain(cls, name, content):
        return cls if name and content else None

    @classmethod
    def create(cls, name, content):
        return cls if name and content else None


class Fachada:
    """A main model for representing interaction with database."""

    @classmethod
    def create(cls, project, users):
        project = Project.get(project)
        return project if project else Project.create(project, users)

    @classmethod
    def load(cls, name):
        code = Module.get(name=name)
        return code and code.content

    @classmethod
    def save(cls, **kwargs):
        code = Module.obtain(**kwargs)
        return code

    @classmethod
    def ismember(cls, project, person):
        if not project:
            return Package.get(person)
        return Project.ismember(project, person)

    @classmethod
    def islogged(cls, project, person):
        project = Project.get(project)
        return project.islogged(person)

    @classmethod
    def logout(cls, project, person):
        project = Project.get(project)
        project.removesession(person)

    @classmethod
    def login(cls, project, person, session=None):
        return

    @classmethod
    def lastcode(cls, lastsession):
        session = lastsession.get()
        person = session.person.get()
        lastcode = person.lastcode
        if lastcode:
            code = lastcode.get()
            name = code.name if code else "nono"
            content = code.content if code else "# empty"
        else:
            name = "nono"
            content = "# empty"

        print("lastcode", person.name, person.lastsession, name, content)
        code = (name, content) if lastcode else ("%s/main.py" % session.person.get().name, "# main")
        return code

    @classmethod
    def _populate_codes(cls, session, persons):
        prj = session.project.get()  # Project.kget(key=session.project)
        if prj.populated:
            return prj.questions
        oquestions = [
            Module.create(name=key, content=value) for key, value in persons
            ]
        print(oquestions)
        prj.populated = True
        prj.questions = oquestions
        prj.put()
        return oquestions

    @classmethod
    def init_db_(cls):

        if "AUTH_DOMAIN" not in os.environ.keys():
            return

    @classmethod
    def _populate_persons(cls, projectname, persons, sprites):
        prj = Project.get(name=projectname)
        if not prj:
            prj = Project.create(name=projectname, sprite=sprites)
        if not prj.persons:
            print("_populate_persons if not prj.persons", ' '.join(persons), projectname)
            prj.persons = ' '.join(persons)
            # prj.put()
        if prj.populated:
            return prj.persons
        new_persons = [
            Package.create(project=prj.key, name=key) for key in persons
            ]
        print(new_persons)
        prj.sessions = {person: False for person in persons}
        prj.populated = True
        # prj.put()
        return new_persons


Fachada.init_db_()
DB = Fachada

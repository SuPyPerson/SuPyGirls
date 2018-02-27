from github import Github
import os.path
import os as op
import model.datasource as dsc

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPackage/SuPyGirls.git"
USERNAME = "carlotolla"
PASSWORD = op.environ["ISME"]


def spike():

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
        return dsc.DS.get_file_contents(project, person) is not None

    @classmethod
    def modules(cls, project):
        return [branch for branch in dsc.DS.get_branches(project)]

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
    def get(cls, project, name):
        """
        Find a package with a given name.
        
        :param project: repository name to be found.
        :param name: package name to be found.
        :return: the package retrieved or None if not found.
        """
        return cls if name and project else None

    @classmethod
    def create(cls, project, name, content=None):
        return cls if project and name and content else None


class Module:
    """
    A module developed by a user
    """
    content = ""

    @classmethod
    def get(cls, project, moduler):
        """
        Find a module with a given name.
        
        :param project: Repository to retrieve.
        :param moduler: package name to be found.
        :return: the package retrieved or None if not found.
        """
        return dsc.DS.get_file_contents(project, moduler)

    @classmethod
    def obtain(cls, project, moduler, content):
        return dsc.DS.update_file(project, moduler, content)

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
    def load(cls, project, person):
        code = Module.get(project, person)
        return code and code.content

    @classmethod
    def save(cls, **kwargs):
        code = Module.obtain(**kwargs)
        return code

    @classmethod
    def modules(cls, project):
        return Project.modules(project)

    @classmethod
    def ismember(cls, project, person):
        if not project:
            return Package.get(project, person)
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
    def login(cls, project, person):
        return Project.ismember(project, person)

    @classmethod
    def init_db_(cls):

        if "AUTH_DOMAIN" not in os.environ.keys():
            return

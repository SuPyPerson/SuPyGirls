from github import Github
import os.path
import os as op

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPerson/SuPyGirls.git"
USERNAME = "carlotolla"
PASSWORD = op.environ["ISME"]

g = Github(USERNAME, PASSWORD)

for repo in g.get_user().get_repos():
    print(repo.name)

rep = g.get_user().get_repo("SuPyGirls")
print(rep.name)
    # repo.edit(has_wiki=False)


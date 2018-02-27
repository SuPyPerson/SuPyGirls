from dulwich import index
from dulwich.client import HttpGitClient
from dulwich.repo import Repo
import os.path
import os as op

LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/git/spg'))
REMOTE_URL = "https://github.com/SuPyPerson/SuPyGirls.git"
USERNAME = "carlotolla"
PASSWORD = op.environ["ISME"]
local_repo = Repo.init(LOCAL_FOLDER, mkdir=True)
remote_repo = HttpGitClient(REMOTE_URL, username=USERNAME, password=PASSWORD)
remote_refs = remote_repo.fetch(REMOTE_URL, local_repo)
local_repo[b"HEAD"] = remote_refs[b"refs/heads/master"]

index_file = local_repo.index_path()
tree = local_repo[b"HEAD"].tree
index.build_index_from_tree(local_repo.path, index_file, local_repo.object_store, tree)
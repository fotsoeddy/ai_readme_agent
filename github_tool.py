import os
from github import Github

def fetch_and_push_readme(new_content: str) -> str:
    token = os.getenv("PAT_TOKEN")  # use PAT_TOKEN env variable
    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH", "main")

    g = Github(token)
    repo = g.get_repo(repo_name)
    file = repo.get_contents("README.md", ref=branch)
    old = file.decoded_content.decode()

    if new_content.strip() == old.strip():
        return "✅ No changes to commit."
    repo.update_file(file.path, "🤖 Daily update by AI agent", new_content, file.sha, branch=branch)
    return "🚀 README updated and pushed."

import os
from dotenv import load_dotenv
from ai_chain import improve_readme_content
from github_tool import fetch_and_push_readme

load_dotenv(dotenv_path=".env")  # Not used in GitHub Actions but useful locally

def run_daily_readme_agent():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH", "main")

    from github import Github
    g = Github(token)
    repo = g.get_repo(repo_name)
    file = repo.get_contents("README.md", ref=branch)
    old_content = file.decoded_content.decode()

    new_content = improve_readme_content(old_content)
    result = fetch_and_push_readme(new_content)
    print(result)

if __name__ == "__main__":
    run_daily_readme_agent()

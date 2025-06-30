from dotenv import load_dotenv
from ai_chain import improve_readme_content
from github_tool import fetch_and_push_readme
from email_reporter import send_commit_email

load_dotenv(dotenv_path=".env")

def run_daily_readme_agent():
    from github import Github
    import os

    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH", "main")

    g = Github(token)
    repo = g.get_repo(repo_name)
    file = repo.get_contents("README.md", ref=branch)
    old_content = file.decoded_content.decode()

    new_content = improve_readme_content(old_content)
    result = fetch_and_push_readme(new_content)

    print(result)

    # Only send email if README was changed
    if "updated" in result.lower():
        subject = f"✅ AI Agent Commit on {repo_name}"
        body = f"The README was updated and committed by the AI agent.\n\n{result}"
        send_commit_email(subject, body)

if __name__ == "__main__":
    run_daily_readme_agent()
